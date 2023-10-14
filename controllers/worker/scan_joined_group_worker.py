from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import BaseWorker
from time import sleep
from random import randrange


class ScanJoinedGroupWorker(BaseWorker):
    def __init__(self, page_id, semaphore_id, account) -> None:
        super().__init__(semaphore_id, account)
        self._pageid = page_id

    @Slot()
    def run(self):
        if not self.take_semaphore_facebook():
            return
        if not self.check_live_facebook(): return
        groups = self.fb_scraper.scan_group_of_page()
        if groups:
            active_id = self._uid if self._pageid == '' else self._pageid
            self.signals.scan_complted.emit(active_id, groups)
