from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import *
from time import sleep
from random import randrange

class GroupPageSignals(BaseSignals):
    allow_page_group = Signal(str, str)

class CheckGroupAllowPage(BaseWorker):
    def __init__(self, semaphore, user_id, group_links) -> None:
        super().__init__(semaphore, user_id)
        self.group_links = group_links
        self.signals = GroupPageSignals()


    def on_update_allow_page_status(self, group_link, interact):
        try:
            self.db_manager.update_group_interact(group_link, interact)
        except Exception as e:
            logging.error('', exc_info=True)

    def connect_signals(self):
        super().connect_signals()
        self.signals.allow_page_group.connect(self.on_update_allow_page_status)

    @Slot()
    def run(self):
        try:
            if not self.take_semaphore_facebook():
                return
            if not self.check_live_facebook():
                return
            
            for group_url in self.group_links:
                status = self.fb_scraper.check_group_allow_post(group_url)
                interact = 'Page' if status else 'Personal'
                self.signals.allow_page_group.emit(group_url, interact)

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