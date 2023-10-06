from PySide6.QtCore import Signal
from PySide6.QtCore import QRunnable, QObject,QMutex,QSemaphore
from facebook_scraper import FacebookScraper

semaphore = {}
chrome_mutex = QMutex()
post_mutex = QMutex()
open_chrom_sem = QSemaphore(2)

class Signals(QObject):
    scan_complted = Signal(str, object)
    scan_keyword_completed = Signal(str, object)
    scan_post_history = Signal(str, str, str, str)
    approved_post = Signal(str, str)
    allow_page_group = Signal(str, str)
    update_status = Signal(str, str)
    update_message = Signal(str, str)
    seeding_status = Signal(str, str, str)

    posted_group_completed = Signal(str,str, str)
    pending_post = Signal(str, str, str)
    scan_today_posts= Signal(str, str, str, str)

class BaseWorker(QRunnable):
    def __init__(self, semaphore_id, uid, password, proxy, secret_2fa) -> None:
        super().__init__()
        self.sema_id = semaphore_id
        self._uid = uid
        self._pw = password
        self._proxy = proxy
        self._secret_2fa = secret_2fa

        self.signals = Signals()

    def take_semaphore_facebook(self):
        self.signals.update_status.emit(self._uid, "Waiting")
        semaphore[self.sema_id].acquire()
        self.signals.update_status.emit(self._uid, 'Opening')
        
        try:
            chrome_mutex.lock()
            self.fb_scraper = FacebookScraper(self._uid, self._pw, self._proxy)
            self.signals.update_message.emit(self._uid, 'Mở chrome...')
        except Exception as e:
            self.signals.update_message.emit(self._uid, 'Chrome error !')
            return False
        finally:
            chrome_mutex.unlock()
        return True
    def __del__(self):
        semaphore[self.sema_id].release()
        self.fb_scraper.close()