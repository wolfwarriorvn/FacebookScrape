from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import BaseWorker
from time import sleep
from common.mailreader import MailReader

class Checkpoint956(BaseWorker):
    def __init__(self,semaphore_id, account) -> None:
        super().__init__(semaphore_id,account)

    @Slot()
    def run(self):
        if not self.take_semaphore_facebook(): return

        if not self.check_live_facebook():
            pass

        mail = MailReader(self.email, self.pass_email)
        mail.read_all()
        self.fb_scraper.checkpoint_956(mail)

        if not self.check_live_facebook():
            pass
        while True:
            if self.fb_scraper.is_brower_closed():
                break
            sleep(1)
