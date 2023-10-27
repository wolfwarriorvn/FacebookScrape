from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import BaseWorker
from time import sleep

class FacebookWorker(BaseWorker):
    def __init__(self,semaphore_id, account) -> None:
        super().__init__(semaphore_id,account)

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
            self.signals.update_message.emit(self._uid, f'{self.__class__.__name__}: {ex}')  
        finally:
            self.exit()