from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import *
from time import sleep
from common.mailreader import MailReader

class Checkpoint956(BaseWorker):
    def __init__(self,semaphore, user_id) -> None:
        super().__init__(semaphore, user_id)

    @Slot()
    def run(self):
        try:
            if not self.take_semaphore_facebook(): 
                return
            
            try:
                self.check_live_facebook()
            except:
                pass
            
            mail = MailReader(self.email, self.pass_email)
            mail.read_all()
            self.fb_scraper.checkpoint_956(mail)

            if self.check_live_facebook():
                self.signals.update_status.emit(self._uid, 'Free')
                self.signals.update_status.emit(self._uid, 'Vượt checkpoint thành công')
            else:
                # self.signals.update_status.emit(self._uid, 'Free')
                self.signals.update_status.emit(self._uid, 'Vượt checkpoint không được')

            while True:
                if self.fb_scraper.is_brower_closed():
                    break
                sleep(1)
            
        except Exception as ex:
            self.signals.update_message.emit(self._uid, f'{self.__class__.__name__}: Error')
            logging.exception('')
        finally:
            self.exit()
