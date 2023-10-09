from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import BaseWorker
from time import sleep
from random import randrange


class ScanPostHistoryWorker(BaseWorker):
    def __init__(self, active_id, loop_scan, semaphore_id, uid, password, proxy=None, secret_2fa=None) -> None:
        super().__init__(semaphore_id, uid, password, proxy, secret_2fa)
        self.active_id = active_id
        self.loop_scan = loop_scan

    @Slot()
    def run(self):
        if not self.take_semaphore_facebook():
            return
        if not self.check_live_facebook(): return
        post_links = self.fb_scraper.get_post_history(self.active_id, self.loop_scan)

        for post_link in post_links:
            group_link = post_link[0:48]
            self.signals.scan_post_history.emit(self.active_id, group_link, post_link, 'Pending')

        self.signals.update_message.emit(self._uid, 'Scan post history completed!!!')