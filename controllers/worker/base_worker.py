from PySide6.QtCore import Signal
from PySide6.QtCore import QRunnable, QObject,QMutex,QSemaphore
from facebook_scraper import FacebookScraper
from model.db_model import AccountInfo
from time import sleep
from facebook_scraper import (
    NoLoginException,
    CheckpointException
)
import logging

semaphore = {}
chrome_mutex = QMutex()
login_mutex = QMutex()
post_mutex = QMutex()
open_chrom_sem = QSemaphore(2)

class BaseSignals(QObject):
    update_status = Signal(str, str)
    update_message = Signal(str, str)


class BaseWorker(QRunnable):
    def __init__(self, semaphore_id, user_id, *args) -> None:
        super().__init__()
        self.sema_id = semaphore_id
        self.user_id = user_id
        self.signals = BaseSignals()
    
    def setup_before_execution(self, db_manager, ui_signals):
        self.ui_signals = ui_signals
        self.db_manager = db_manager
        accounts = db_manager.get_account_info(self.user_id)
        self._uid = accounts.uid
        self._pw = accounts.password
        self._proxy = accounts.proxy
        self.email = accounts.email
        self.pass_email = accounts.pass_email
        self._secret_2fa = accounts.secret_2fa
        self.cookie = accounts.cookie

    def update_message_dashboard(self, uid, message):
        try:
            self.db_manager.update_account_message(uid, message)
            self.ui_signals.update_dashboard.emit()
        except Exception as e:
            logging.error('', exc_info=True)

    def update_status_dashboard(self, uid, status):
        try:
            self.db_manager.update_account_status(uid, status)
            self.ui_signals.update_dashboard.emit()
        except Exception as e:
            logging.error('', exc_info=True)

    def connect_signals(self):
        self.signals.update_status.connect(self.update_status_dashboard)
        self.signals.update_message.connect(self.update_message_dashboard)
        
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
            self.signals.update_status.emit(self._uid, 'Busy')
            self.signals.update_message.emit(self._uid, 'Already Logging!')
            
            status = True
        except NoLoginException:
            self.signals.update_status.emit(self._uid, 'Unlogin')
            self.signals.update_message.emit(self._uid, 'Login facebook again!')
        except CheckpointException as ex:
            self.signals.update_status.emit(self._uid, f'{ex}')
            self.signals.update_message.emit(self._uid, 'Checkpoint!')
        except Exception as ex:
            self.signals.update_message.emit(self._uid, f'{type(ex).__name__}: {ex}!')
        finally:
            login_mutex.unlock()

        return status
    
    def take_semaphore_facebook(self):
        status = False
        semaphore[self.sema_id].acquire()
        
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
    
    def exit(self):
        # self.signals.update_status.emit(self._uid, 'Free')
        semaphore[self.sema_id].release()
        if self.fb_scraper:
            self.fb_scraper.close()   
    # def __del__(self):
    #     self.signals.update_status.emit(self._uid, 'Free')
    #     semaphore[self.sema_id].release()
    #     if self.fb_scraper:
    #         self.fb_scraper.close()