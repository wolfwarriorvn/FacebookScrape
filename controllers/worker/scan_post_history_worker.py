from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import *
from time import sleep
from random import randrange

class ScanPostHistorySignals(BaseSignals):
    scan_post_history = Signal(str, str, str, str)

class ScanPostHistoryWorker(BaseWorker):
    def __init__(self, semaphore, user_id, loop_scan) -> None:
        super().__init__(semaphore, user_id)
        self.loop_scan = loop_scan
        self.signals = ScanPostHistorySignals()

    def setup_before_execution(self, db_manager, ui_signals):
        super().setup_before_execution(db_manager, ui_signals)
        self.active_id = self.db_manager.get_account_pageid(self.user_id)

    def on_save_post_history(self, active_id, group_link, post_link, status):
        try:
            self.db_manager.add_post_history(
                active_id, group_link, post_link, status)
        except Exception as e:
            logging.error('', exc_info=True)

    def connect_signals(self):
        super().connect_signals()
        self.signals.scan_post_history.connect(self.on_save_post_history)

    @Slot()
    def run(self):
        try:
            if not self.take_semaphore_facebook():
                return
            if not self.check_live_facebook(): return
            post_links = self.fb_scraper.get_post_history(self.active_id, self.loop_scan)

            for post_link in post_links:
                group_link = post_link[0:48]
                self.signals.scan_post_history.emit(self.active_id, group_link, post_link, 'Pending')
                print(group_link)

            self.signals.update_message.emit(self._uid, 'Scan post history completed!!!')
            self.signals.update_status.emit(self._uid, 'Free')

        except NoLoginException:
            self.signals.update_status.emit(self._uid, 'Unlogin')
        except CheckpointException as ex:
            self.signals.update_status.emit(self._uid, f'{ex}')
        except :
            self.signals.update_status.emit(self._uid, 'Free')
            self.signals.update_message.emit(self._uid, f'{self.__class__.__name__}: Error')
            logging.exception('')
        finally:
            self.exit()