from PySide6.QtCore import QObject
from PySide6.QtCore import Signal, Slot
from PySide6.QtCore import QThreadPool, QSemaphore

from model.model import DatabaseModel

from controllers.worker import *
from common.payload import *

import uuid
import random
import logging
from controllers.worker.base_worker import semaphore


class AccountInfo:
    def __init__(self, uid, pw, proxy) -> None:
        self.uid = uid
        self.pw = pw
        self.proxy = proxy


class MySignals(QObject):
    # Edit account signal
    update_dashboard = Signal()

    # Pages Manage
    get_accounts = Signal()
    get_accounts_completed = Signal(object)

    # facebook
    post_event = Signal(object, object)
    scan_group_by_keyword = Signal(str, str, int)
    check_approval_post = Signal(str, object)
    check_group_allow_page = Signal(str, object)
    scan_group_completed = Signal()
    scan_post_history = Signal(object, int, int)
    seeding_action = Signal(object, object)
    outof_free_groups = Signal(int)

    #login
    #checkpoint 
    checkpoint_956 = Signal(object)
class DatabaseWorker(QObject):
    finished = Signal()
    result = Signal(object, str)  # First argument for the result, second for error

    def __init__(self, operation, data, callback):
        super().__init__()
        self.operation = operation
        self.data = data
        self.callback = callback

    def run(self):
        try:
            result = self.operation(self.data) if self.data else self.operation()
            self.result.emit(result, None)
        except Exception as e:
            self.result.emit(None, str(e))
        finally:
            self.finished.emit()

class DbSignals(QObject):
    # Proxy table
    get_free_group = Signal(str)
    get_free_group_completed = Signal(int)


class Controller(QObject):
    signals = MySignals()
    db_signals = DbSignals()
    database_operation = Signal(str, object, object)

    def __init__(self, model: DatabaseModel):
        super().__init__()
        self.pool = QThreadPool.globalInstance()
        self._model = model

        self.database_operation.connect(self.handle_operation)

        self.signals.checkpoint_956.connect(self.init_thread_checkpoint_956)
        self.signals.check_approval_post.connect(
            self.init_thread_check_approval_post)
        self.signals.check_group_allow_page.connect(
            self.init_thread_check_group_allow_page)

        self.signals.post_event.connect(self.init_thread_post)
        self.signals.scan_group_by_keyword.connect(self.scan_group_by_keyword)
        self.signals.scan_post_history.connect(self.on_scan_post_history)
        self.signals.seeding_action.connect(self.init_thread_seeding_action)
        self.db_signals.get_free_group.connect(self.on_get_free_group)


    def handle_operation(self, operation_type, callback, args):
        try:
            operation_method = getattr(self._model, operation_type, None)
            if operation_method:
                result = operation_method(**args)
                callback(result, None)
            else:
                raise ValueError(f"Unhandled operation type: {operation_type}")
        except Exception as e:
            callback(None, str(e))

    
    def on_get_free_group(self, type_groups):
        free_group_links = self._model.get_group_free(type_groups)
        self.db_signals.get_free_group_completed.emit(len(free_group_links))

    def on_add_proxy(self, proxy, proxy_zip):
        try:
            self._model.add_proxy(proxy, proxy_zip)
            self.db_signals.proxy_add_completed.emit()
        except Exception as e:
            logging.error('', exc_info=True)

    def init_thread_post(self, uids, setting: PostSetting):
        sema_id = self.genarate_semaphore(setting.threads)
        free_group_links = self._model.get_group_free(setting.type_group)
        total_post = len(uids) * setting.post_count
        if total_post > len(free_group_links):
            logging.warning('Outof free nick')
            return
        set_free_groups = set(free_group_links)
        set_picked = set()

        for uid in uids:
            try:
                account = self._model.get_account_info(uid)
                pageID = self._model.get_account_pageid(uid)
                activeID = uid if pageID == '' else pageID

                select_groups = random.sample(
                    sorted(set_free_groups.difference(set_picked)), setting.post_count)
                set_picked.update(select_groups)

                worker = PostGroupWorker(
                    select_groups, setting, activeID, sema_id, account)
                worker.setAutoDelete(True)
                worker.signals.update_status.connect(
                    self.update_status_dashboard)
                worker.signals.update_message.connect(
                    self.update_mesage_dashboard)
                worker.signals.posted_group_completed.connect(
                    self.post_completed)
                worker.signals.scan_today_posts.connect(
                    self.on_save_post_history)
                self.pool.start(worker)

            except Exception as ex:
                self.update_mesage_dashboard(uid, f'{type(ex).__name__}: {ex}')
                continue

    def post_completed(self, pageid, group_link, status):
        try:
            self._model.update_group_posted_status(pageid, group_link, status)
        except Exception as e:
            logging.error('', exc_info=True)
            pass

    def init_thread_checkpoint_956(self, list_uids):
        sema_id = self.genarate_semaphore(1)
        for uid in list_uids:
            try:
                account = self._model.get_account_info(uid)

                worker = Checkpoint956(sema_id,account)
                worker.signals.update_status.connect(
                    self.update_status_dashboard)
                worker.signals.update_message.connect(
                    self.update_mesage_dashboard)
                worker.setAutoDelete(True)
                self.pool.start(worker)

            except Exception as ex:
                self.update_mesage_dashboard(uid, f'{type(ex).__name__}: {ex}')

    def init_thread_seeding_action(self, uids, setting: SeedingSetting):
        sema_id = self.genarate_semaphore(setting.threads)
        if setting.auto_getlink:
            setting.posted_links = self._model.get_post_approved_link()
        for uid in uids:
            try:
                account = self._model.get_account_info(uid)
                if setting.auto_getlink:
                    liked_links = self._model.get_seeding_liked_link(uid)
                    set_available_links = set(
                        setting.posted_links).difference(set(liked_links))
                    if len(set_available_links) < setting.seedings:
                        self.update_mesage_dashboard(
                            uid, 'Không đủ link để like. Số link còn lại: {}'.format(len(set_available_links)))
                        continue

                    available_links = random.sample(
                        sorted(set_available_links), setting.seedings)
                else:
                    available_links = setting.posted_links

                worker = SeedingWorker(
                    available_links, setting, sema_id, account)
                worker.signals.update_status.connect(
                    self.update_status_dashboard)
                worker.signals.update_message.connect(
                    self.update_mesage_dashboard)
                worker.signals.seeding_status.connect(
                    self.on_update_seeding_status)
                worker.setAutoDelete(True)
                self.pool.start(worker)
            except Exception as ex:
                self.update_mesage_dashboard(uid, f'{type(ex).__name__}: {ex}')
                continue

    def on_update_seeding_status(self, uid, href, action):
        try:
            if action == 'Liked':
                self._model.update_post_liked_counts(href)
            elif action == 'Commented':
                self._model.update_post_commented_counts(href)

            self._model.add_seeding_action(uid, href, action)
        except Exception as e:
            logging.error('', exc_info=True)

    def init_thread_check_group_allow_page(self, uid, group_links):
        sema_id = self.genarate_semaphore(1)
        try:
            account = self._model.get_account_info(uid)

            worker = CheckGroupAllowPage(
                group_links,sema_id, account)
            worker.setAutoDelete(True)
            worker.signals.allow_page_group.connect(
                self.on_update_allow_page_status)
            #command signal
            worker.signals.update_status.connect(
                self.update_status_dashboard)
            worker.signals.update_message.connect(
                self.update_mesage_dashboard)
            self.pool.start(worker)
        except Exception as e:
            logging.error('', exc_info=True)

    def on_update_allow_page_status(self, group_link, interact):
        try:
            self._model.update_group_interact(group_link, interact)
        except Exception as e:
            logging.error('', exc_info=True)

    def init_thread_check_approval_post(self, uid, pending_posts):
        sema_id = self.genarate_semaphore(1)
        try:
            account = self._model.get_account_info(uid)

            worker = CheckApprovalPost(
                pending_posts, sema_id, account)
            worker.setAutoDelete(True)
            worker.signals.approved_post.connect(self.on_update_approve_status)

            #command signal
            worker.signals.update_status.connect(
                self.update_status_dashboard)
            worker.signals.update_message.connect(
                self.update_mesage_dashboard)
            self.pool.start(worker)
            
        except Exception as ex:
            self.update_mesage_dashboard(uid, f'{type(ex).__name__}: {ex}')

    def on_update_approve_status(self, pending_post, status):
        try:
            self._model.update_post_status(pending_post, status)
        except Exception as e:
            logging.error('', exc_info=True)

    def on_scan_post_history(self, uids, loop_scan, sync_nick):
        sema_id = self.genarate_semaphore(sync_nick)
        for uid in uids:
            try:
                account = self._model.get_account_info(uid)
                active_id = self._model.get_account_pageid(uid)

                worker = ScanPostHistoryWorker(
                    active_id, loop_scan, sema_id, account)
                worker.signals.scan_post_history.connect(
                    self.on_save_post_history)
                
                #command signal
                worker.signals.update_status.connect(
                    self.update_status_dashboard)
                worker.signals.update_message.connect(
                    self.update_mesage_dashboard)
                worker.setAutoDelete(True)
                self.pool.start(worker)
                
            except Exception as ex:
                self.update_mesage_dashboard(uid, f'{type(ex).__name__}: {ex}')

    def on_save_post_history(self, active_id, group_link, post_link, status):
        try:
            self._model.add_post_history(
                active_id, group_link, post_link, status)
        except Exception as e:
            logging.error('', exc_info=True)

    def login_chrome(self, selected_uids):
        sema_id = self.genarate_semaphore(1)
        for uid in selected_uids:
            try:
                account = self._model.get_account_info(uid)

                worker = LoginFacebookWorker(sema_id, account)
                worker.signals.update_status.connect(
                        self.update_status_dashboard)
                worker.signals.update_message.connect(
                        self.update_mesage_dashboard)
                worker.setAutoDelete(True)
                self.pool.start(worker)

            except Exception as ex:
                self.update_mesage_dashboard(uid, f'{type(ex).__name__}: {ex}')

    def open_chrome(self, selected_uids):
        sema_id = self.genarate_semaphore(100)
        for uid in selected_uids:
            try:
                account = self._model.get_account_info(uid)

                worker = FacebookWorker(sema_id,account)
                worker.signals.update_status.connect(
                    self.update_status_dashboard)
                worker.signals.update_message.connect(
                    self.update_mesage_dashboard)
                worker.setAutoDelete(True)
                self.pool.start(worker)

            except Exception as ex:
                self.update_mesage_dashboard(uid, f'{type(ex).__name__}: {ex}')

    def update_mesage_dashboard(self, uid, message):
        try:
            self._model.update_account_message(uid, message)
            self.signals.update_dashboard.emit()
        except Exception as e:
            logging.error('', exc_info=True)

    def update_status_dashboard(self, uid, status):
        try:
            self._model.update_account_status(uid, status)
            self.signals.update_dashboard.emit()
        except Exception as e:
            logging.error('', exc_info=True)

    def scan_group_by_keyword(self, uid, keyword, loop_scan):
        sema_id = self.genarate_semaphore(1)
        try:
            account = self._model.get_account_info(uid)

            worker = ScanGroupKeywordWorker(
                keyword, loop_scan, sema_id, account)
            worker.signals.update_status.connect(
                self.update_status_dashboard)
            worker.signals.update_message.connect(
                self.update_mesage_dashboard)
            worker.setAutoDelete(True)
            worker.signals.scan_keyword_completed.connect(
                self.scan_keyword_completed)
            self.pool.start(worker)
        except Exception as ex:
            self.update_mesage_dashboard(uid, f'{type(ex).__name__}: {ex}')

    def scan_keyword_completed(self, uid, groups):
        talbe_name = 'groups_' + uid
        try:
            self._model.create_group_table(talbe_name)
            self._model.add_group_scan(talbe_name,
                                       groups)
        except Exception as e:
            logging.error('', exc_info=True)

    Slot(str)
    def get_account_info(self, indexs):
        try:
            if len(indexs) == 1:
                uid, pw, proxy = self._model.get_account_info(indexs[0])
                self.signals.get_account_completed.emit(
                    AccountInfo(uid, pw, proxy))
        except Exception as e:
            logging.error('', exc_info=True)

    def genarate_semaphore(self, resources):
        sema_id = uuid.uuid4()
        semaphore[sema_id] = QSemaphore(resources)
        return sema_id
