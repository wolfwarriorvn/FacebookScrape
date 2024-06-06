from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import *
from time import sleep
import logging
class FacebookWorker(BaseWorker):
    def __init__(self,semaphore, user_id) -> None:
        super().__init__(semaphore, user_id)

    @Slot()
    def run(self):
        try:
            if not self.take_semaphore_facebook(): return

            status = self.check_live_facebook()

            while True:
                if self.fb_scraper.is_brower_closed():
                    break
                sleep(1)
            if status:
                self.signals.update_status.emit(self._uid, 'Free')
                
        except Exception as ex:
            self.signals.update_message.emit(self._uid, f'{self.__class__.__name__}: Error')
            logging.exception('')
        finally:
            self.exit()