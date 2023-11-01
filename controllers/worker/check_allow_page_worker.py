from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import *
from time import sleep
from random import randrange


class CheckGroupAllowPage(BaseWorker):
    def __init__(self, group_links, semaphore_id, account) -> None:
        super().__init__(semaphore_id, account)
        self.group_links = group_links

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