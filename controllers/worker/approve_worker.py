from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import *
from time import sleep
from random import randrange
from common.payload import ThreadAprovalPayload

class ApproveSignals(BaseSignals):
    post_request = Signal(object)

class ApproveWorker(BaseWorker):
    def __init__(self, semaphore, user_id, thread_settings: ThreadAprovalPayload) -> None:
        super().__init__(semaphore, user_id)
        self.thread_settings = thread_settings
        self.signals = ApproveSignals()

    def on_post_request(self, aprove_requests):
        try:
            self.db_manager.add_approve_request(aprove_requests)
        except Exception as e:
            logging.error('', exc_info=True)
    def connect_signals(self):
        super().connect_signals()
        self.signals.post_request.connect(self.on_post_request)

    @Slot()
    def run(self):
        try:
            if not self.take_semaphore_facebook():
                return
            if not self.check_live_facebook(): return

            for group_approve in self.thread_settings.approval_settings:
                post_requests = self.fb_scraper.approve_pending_request(group_approve , self.thread_settings.post_count)
                self.signals.post_request.emit(post_requests)


        except NoLoginException:
            self.signals.update_status.emit(self._uid, 'Unlogin')
        except CheckpointException as ex:
            self.signals.update_status.emit(self._uid, f'{ex}')
        except :
            self.signals.update_status.emit(self._uid, 'Free')
            self.signals.update_message.emit(self._uid, f'{self.__class__.__name__}: Error')
            logging.exception('')
        finally:
            self.exit()