from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import BaseWorker
from time import sleep

class LoginFacebookWorker(BaseWorker):
    def __init__(self, semaphore_id, uid, password, proxy, secret_2fa) -> None:
        super().__init__(semaphore_id, uid, password, proxy, secret_2fa)

    @Slot()
    def run(self):
        if not self.take_semaphore_facebook(): return

        try:
            self.signals.update_message.emit(self._uid, 'Đang Logging chrome...')
            self.fb_scraper.login_with_userpass(self._secret_2fa)


            self.check_live_facebook()
        except Exception as e:
            print("Login error: ", e)

        while True:
            if self.fb_scraper.is_brower_closed():
                break
            sleep(1)
