

from PyQt6.QtCore import QRunnable, QObject, QThreadPool, QThread
from PySide6.QtCore import Signal, Slot

from facebook_scraper import FacebookScraper
from time import sleep

class FacebookWorker(QRunnable):
    def __init__(self, uid, pw, proxy=None) -> None:
        super().__init__()
        self._uid = uid
        self._pw = pw
        self._proxy = proxy
        
    @Slot()
    def run(self):
        print("Uid start: ", self._uid)
        print("Hello world from thread", QThread.currentThread())
        self.fb_scraper = FacebookScraper(self._uid, self._pw, self._proxy)
        while True:
            if self.fb_scraper.is_brower_closed():
                break
            sleep(5)
        print("Uid stop: ", self._uid)