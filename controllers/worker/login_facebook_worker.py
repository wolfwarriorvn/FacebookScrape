from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import *
from time import sleep
from facebook_scraper import (
    NoLoginException,
    CheckpointException
)

class LoginFacebookWorker(BaseWorker):
    def __init__(self, semaphore_id, account) -> None:
        super().__init__(semaphore_id, account)

    @Slot()
    def run(self):
        try:
            if not self.take_semaphore_facebook(): return

            try:
                self.fb_scraper.open_url('https://www.facebook.com/')
                
            except NoLoginException:
                self.signals.update_message.emit(self._uid, 'Đang Logging chrome...')
                self.fb_scraper.login_with_userpass(self._secret_2fa)
            except:
                pass

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

