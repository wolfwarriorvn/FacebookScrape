from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import *
from time import sleep
from random import randrange

class CheckApprovalSignals(BaseSignals):
    approved_post = Signal(str, str)

class CheckApprovalPost(BaseWorker):
    def __init__(self, semaphore, user_id, pending_posts) -> None:
        super().__init__(semaphore, user_id)
        self.pending_posts = pending_posts
        self.signals = CheckApprovalSignals()

    def on_update_approve_status(self, pending_post, status):
        try:
            self.db_manager.update_post_status(pending_post, status)
        except Exception as e:
            logging.error('', exc_info=True)

    def connect_signals(self):
        super().connect_signals()
        self.signals.approved_post.connect(self.on_update_approve_status)

    @Slot()
    def run(self):
        try:
            if not self.take_semaphore_facebook():
                return
            if not self.check_live_facebook():
                return
            
            for post in self.pending_posts:
                is_approved = self.fb_scraper.check_approval_post(post)
                
                self.signals.approved_post.emit(post, 'Approved' if is_approved else 'Pending')

            self.signals.update_status.emit(self._uid, 'Free')
            
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
