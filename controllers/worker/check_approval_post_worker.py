from PySide6.QtCore import Signal, Slot
from controllers.worker.base_worker import BaseWorker
from time import sleep
from random import randrange


class CheckApprovalPost(BaseWorker):
    def __init__(self,pending_posts, semaphore_id, uid, password, proxy=None, secret_2fa=None) -> None:
        super().__init__(semaphore_id, uid, password, proxy, secret_2fa)
        self.pending_posts = pending_posts

    @Slot()
    def run(self):
        if not self.take_semaphore_facebook():
            return
        
        for post in self.pending_posts:
            is_approved = self.fb_scraper.check_approval_post(post)
            if is_approved:
                self.signals.approved_post.emit(post, 'Approved')