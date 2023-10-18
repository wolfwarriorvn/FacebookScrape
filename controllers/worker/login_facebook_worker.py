from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import BaseWorker
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
        if not self.take_semaphore_facebook(): return

        try:
            self.fb_scraper.open_url('https://www.facebook.com/')
            
        except NoLoginException:
            self.signals.update_message.emit(self._uid, 'Đang Logging chrome...')
            self.fb_scraper.login_with_userpass(self._secret_2fa)
        except:
            pass
        finally:
            self.check_live_facebook()
            
        while True:
            if self.fb_scraper.is_brower_closed():
                break
            sleep(1)
