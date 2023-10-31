from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import *
from time import sleep
from random import randrange


class ScanGroupKeywordWorker(BaseWorker):
    def __init__(self, keyword, loop_scan, semaphore_id, account) -> None:
        super().__init__(semaphore_id, account)
        self.keyword = keyword
        self.loop_scan = loop_scan

    @Slot()
    def run(self):
        try:
            if not self.take_semaphore_facebook():
                return
            if not self.check_live_facebook(): return
            groups = self.fb_scraper.scan_group_by_keyword(self.keyword, self.loop_scan)
            if groups:
                self.signals.scan_keyword_completed.emit(self._uid, groups)

            self.signals.update_status.emit(self._uid, 'Free')

        except Exception as ex:
            self.signals.update_message.emit(self._uid, f'{self.__class__.__name__}: Error')
            logging.exception('')
        finally:
            self.exit()