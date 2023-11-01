from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import *
from time import sleep
from random import randrange


class ScanPostHistoryWorker(BaseWorker):
    def __init__(self, active_id, loop_scan, semaphore_id, account) -> None:
        super().__init__(semaphore_id, account)
        self.active_id = active_id
        self.loop_scan = loop_scan

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