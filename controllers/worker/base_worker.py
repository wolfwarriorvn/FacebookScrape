from PySide6.QtCore import Signal
from PySide6.QtCore import QRunnable, QObject,QMutex,QSemaphore
from facebook_scraper import FacebookScraper
from model.model import AccountInfo
from time import sleep
from facebook_scraper import (
    NoLoginException,
    CheckpointException
)

semaphore = {}
chrome_mutex = QMutex()
login_mutex = QMutex()
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
    def __init__(self, semaphore_id, accounts: AccountInfo) -> None:
        super().__init__()
        self.sema_id = semaphore_id
        self._uid = accounts.uid
        self._pw = accounts.password
        self._proxy = accounts.proxy
        self.email = accounts.email
        self.pass_email = accounts.pass_email
        self._secret_2fa = accounts.secret_2fa
        self.cookie = accounts.cookie
        self.signals = Signals()
    def checkpoint(self):
        try:
            if self.fb_scraper.checkpoint():
                self.signals.update_message.emit(self._uid, 'Checkpoint!')
                return True
        except Exception as e:
            return True
        return False
    def check_live_facebook(self):
        status = False
        try:
            login_mutex.lock()
            # self.fb_scraper.open_url('https://www.facebook.com/')
            self.fb_scraper.check_live()
            
            self.signals.update_message.emit(self._uid, 'Already Logging!')
            status = True
        except NoLoginException:
            self.signals.update_message.emit(self._uid, 'Login facebook again!')
        except CheckpointException:
            self.signals.update_message.emit(self._uid, 'Checkpoint!')
        except Exception as ex:
            self.signals.update_message.emit(self._uid, f'{type(ex).__name__}: {ex}!')
        finally:
            login_mutex.unlock()

        return status
    def take_semaphore_facebook(self):
        status = False
        self.signals.update_status.emit(self._uid, "Waiting")
        semaphore[self.sema_id].acquire()
        self.signals.update_status.emit(self._uid, 'Opening')
        
        try:
            chrome_mutex.lock()
            self.signals.update_message.emit(self._uid, 'Đang mở chrome!')
            self.fb_scraper = FacebookScraper(self._uid, self._pw, self._proxy, self.cookie)
            status = True

        except Exception as ex:
            self.signals.update_message.emit(self._uid, f'{type(ex).__name__}: {ex}!')
        finally:
            chrome_mutex.unlock()
        return status
    def __del__(self):
        self.signals.update_status.emit(self._uid, 'Closed')
        semaphore[self.sema_id].release()
        if self.fb_scraper:
            self.fb_scraper.close()