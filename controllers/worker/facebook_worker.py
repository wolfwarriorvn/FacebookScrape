from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import BaseWorker
from time import sleep


class FacebookWorker(BaseWorker):
    def __init__(self, semaphore_id, uid, password, proxy=None, secret_2fa=None) -> None:
        super().__init__(semaphore_id, uid, password, proxy, secret_2fa)

    @Slot()
    def run(self):
        if not self.take_semaphore_facebook(): return
        try:
            if not self.fb_scraper.check_login():
                self.signals.update_message.emit(self._uid, 'Logging chrome...')
                self.fb_scraper.login_with_userpass(self._secret_2fa)
        except Exception as e:
            print("Thread error: ", e)

        while True:
            if self.fb_scraper.is_brower_closed():
                self.signals.update_status.emit(self._uid, 'Closed')
                self.signals.update_message.emit(self._uid, 'Đóng chrome')
                break
            sleep(1)
