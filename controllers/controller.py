from PySide6.QtCore import QObject
from PySide6.QtCore import Signal, Slot
from PySide6.QtCore import QThreadPool, QSemaphore

from model.db_model import DatabaseModel

from controllers.worker import *
from common.payload import *

import uuid
import random
import logging
from controllers.worker.base_worker import semaphore
from model.db_model import DatabaseRequest

from model.database_manager import DatabaseManager
from model.request import InsertRequest
from controllers.worker.database_worker import DatabaseWorker


class TastSignals(QObject):
    # Edit account signal
    open_chrome = Signal(object)
    login_chrome = Signal(object)

    # facebook
    post_groups = Signal(object, object, object)
    scan_group_by_keyword = Signal(str, str, int)
    check_approval_post = Signal(str, object)
    check_group_allow_page = Signal(str, object)
    scan_group_completed = Signal()
    scan_post_history = Signal(object, int, int)
    seeding_action = Signal(object, object)
    outof_free_groups = Signal(int)
    approval = Signal(object, object)

    # login
    # checkpoint
    checkpoint_956 = Signal(object)


class UiSignals(QObject):
    update_dashboard = Signal()


class Controller(QObject):
    database_operation = Signal(str, object, object)
    action_triggered = Signal(str, object)
    task_signals = TastSignals()
    ui_signals = UiSignals()

    def __init__(self, db_model: DatabaseModel):
        super().__init__()
        self.thead_pool = QThreadPool.globalInstance()
        self.db_model = db_model
        self.db_manager = DatabaseManager(self.db_model)

        self.database_operation.connect(self.handle_operation)
        self.task_signals.open_chrome.connect(self.handle_open_chrome)
        self.task_signals.post_groups.connect(self.handle_post_groups)
        self.task_signals.checkpoint_956.connect(self.handle_checkpoint_956)
        self.task_signals.check_approval_post.connect(
            self.handle_check_approval_post)
        self.task_signals.check_group_allow_page.connect(
            self.handle_check_group_allow_page)
        self.task_signals.scan_group_by_keyword.connect(
            self.handle_scan_group_by_keyword)
        self.task_signals.scan_post_history.connect(
            self.handle_scan_post_history)
        self.task_signals.seeding_action.connect(self.handle_seeding_action)
        self.task_signals.approval.connect(self.handle_approval)
        self.task_signals.login_chrome.connect(self.handle_login_chrome)

    Slot(str, QObject, object)

    def handle_operation(self, operation_type, callback, request):
        db_worker = DatabaseWorker(operation_type, request)
        # db_worker.signal.result.connect(callback)
        db_worker.signal.result.connect(
            lambda result, error: callback(result, error))
        db_worker.setAutoDelete(True)
        self.thead_pool.start(db_worker)

    def start_worker(self, worker_class, semaphore, user_id, *args):
        try:
            
            worker = worker_class(semaphore, user_id, *args)
            worker.setup_before_execution(self.db_manager, self.ui_signals)
            worker.connect_signals()

            self.thead_pool.start(worker)
        except Exception as ex:
            self.update_message_dashboard(
                user_id, f'{type(ex).__name__}: {ex}')
            logging.error(f'{type(ex).__name__}: {ex}', exc_info=True)

    def handle_open_chrome(self, user_ids):
        MAX_CHROME_OPEN = 10
        semaphore = self.genarate_semaphore(MAX_CHROME_OPEN)
        for user_id in user_ids:
            self.start_worker(FacebookWorker, semaphore, user_id)

    def handle_login_chrome(self, user_ids):
        semaphore = self.genarate_semaphore(max_resources=1)
        for user_id in user_ids:
            self.start_worker(LoginFacebookWorker, semaphore, user_id)

    def handle_post_groups(self, user_ids, free_groups, setting: PostSetting):
        semaphore = self.genarate_semaphore(setting.threads)
        for user_id in user_ids:
            group_links = [free_groups.pop(random.randint(
                0, len(free_groups)-1)) for _ in range(setting.post_count)]

            self.start_worker(PostGroupWorker, semaphore,
                              user_id, group_links, setting)

    def handle_checkpoint_956(self, user_ids):
        semaphore = self.genarate_semaphore(1)
        for user_id in user_ids:
            self.start_worker(Checkpoint956, semaphore, user_id)

    def handle_seeding_action(self, user_ids, settings: SeedingSetting):
        semaphore = self.genarate_semaphore(settings.threads)
        for user_id in user_ids:
            self.start_worker(SeedingWorker, semaphore, user_id, settings)

    def handle_check_group_allow_page(self, user_id, group_links):
        semaphore = self.genarate_semaphore(max_resources=1)
        self.start_worker(CheckGroupAllowPage, semaphore, group_links)

    def handle_check_approval_post(self, user_id, pending_posts):
        semphore = self.genarate_semaphore(max_resources=1)
        self.start_worker(CheckApprovalPost, semaphore, pending_posts)

    def handle_scan_post_history(self, user_ids, loop_scan, sync_nick):
        semaphore = self.genarate_semaphore(max_resources=sync_nick)
        for user_id in user_ids:
            self.start_worker(ScanGroupKeywordWorker, loop_scan)

    def handle_approval(self, user_ids, settings: ThreadAprovalPayload):
        semaphore = self.genarate_semaphore(max_resources=10)
        for user_id in user_ids:
            self.start_worker(ApproveWorker, semaphore, user_id, settings)

    def handle_scan_group_by_keyword(self, user_id, keyword, loop_scan):
        semaphore = self.genarate_semaphore(1)

        self.start_worker(ScanGroupKeywordWorker, semaphore,
                          user_id, keyword, loop_scan)

    def genarate_semaphore(self, max_resources):
        sema_id = uuid.uuid4()
        semaphore[sema_id] = QSemaphore(max_resources)
        return sema_id

    def update_message_dashboard(self, user_id, message):
        try:
            self.db_manager.update_account_message(user_id, message)
            self.ui_signals.update_dashboard.emit()
        except Exception as e:
            logging.error('', exc_info=True)