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

from model.account_manager import AccountManager
from model.post_manager import PostManager
from model.proxy_namager import ProxyManager
from model.seeding import SeedingManager
from model.group_tita_manager import GroupTitaManager
from model.request import InsertRequest
from controllers.worker.database_worker import DatabaseWorker

class TastSignals(QObject):
    # Edit account signal
    update_dashboard = Signal()
    open_chrome = Signal(object)

    # facebook
    post_groups = Signal(object, object)
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

class Controller(QObject):
    database_operation = Signal(str, object, object)
    action_triggered = Signal(str, object)
    task_signals = TastSignals()

    def __init__(self, db_model: DatabaseModel):
        super().__init__()
        self.thead_pool = QThreadPool.globalInstance()
        self.db_model = db_model
        self.account_manager = AccountManager(self.db_model)
        self.seeding_manager = SeedingManager(self.db_model)
        self.group_tita_manager = GroupTitaManager(self.db_model)
        self.post_manager = PostManager(self.db_model)
        self.proxy_manager = ProxyManager(self.db_model)

        self.database_operation.connect(self.handle_operation)
        self.task_signals.open_chrome.connect(self.handle_open_chrome)
        self.task_signals.post_groups.connect(self.handle_post_groups)
        self.task_signals.checkpoint_956.connect(self.handle_checkpoint_956)
        self.task_signals.check_approval_post.connect(
            self.handle_check_approval_post)
        self.task_signals.check_group_allow_page.connect(
            self.handle_check_group_allow_page)
        self.task_signals.scan_group_by_keyword.connect(self.handle_scan_group_by_keyword)
        self.task_signals.scan_post_history.connect(self.handle_scan_post_history)
        self.task_signals.seeding_action.connect(self.handle_seeding_action)

    Slot(str, QObject, object)
    def handle_operation(self, operation_type, callback, request):
        db_worker = DatabaseWorker(operation_type,request )
        # db_worker.signal.result.connect(callback)
        db_worker.signal.result.connect(lambda result, error: callback(result, error))
        db_worker.setAutoDelete(True)
        self.thead_pool.start(db_worker)

    
    def handle_open_chrome(self, uids):
        MAX_ACCOUTS_OPEN = 10 
        sema_id = self.genarate_semaphore(MAX_ACCOUTS_OPEN)
        for uid in uids:
            try:
                account = self.account_manager.get_account_info(uid)
                worker = FacebookWorker(sema_id,account)
                worker.signals.update_status.connect(
                        self.update_status_dashboard)
                worker.signals.update_message.connect(
                        self.update_mesage_dashboard)
                worker.setAutoDelete(True)
                self.thead_pool.start(worker)
            except Exception as ex:
                self.update_mesage_dashboard(uid, f'{type(ex).__name__}: {ex}')

    def handle_post_groups(self, uids, setting: PostSetting):
        sema_id = self.genarate_semaphore(setting.threads)
        free_group_links = self.group_tita_manager.get_group_free(setting.type_group)
        total_post = len(uids) * setting.post_count
        if total_post > len(free_group_links):
            logging.warning('Outof free nick')
            return
        set_free_groups = set(free_group_links)
        set_picked = set()

        for uid in uids:
            try:
                account = self.account_manager.get_account_info(uid)
                pageID = self.account_manager.get_account_pageid(uid)
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
                self.thead_pool.start(worker)

            except Exception as ex:
                self.update_mesage_dashboard(uid, f'{type(ex).__name__}: {ex}')
                continue

    def post_completed(self, pageid, group_link, status):
        try:
            self.group_tita_manager.update_group_posted_status(pageid, group_link, status)
        except Exception as e:
            logging.error('', exc_info=True)
            pass

    def handle_checkpoint_956(self, list_uids):
        sema_id = self.genarate_semaphore(1)
        for uid in list_uids:
            try:
                account = self.account_manager.get_account_info(uid)

                worker = Checkpoint956(sema_id,account)
                worker.signals.update_status.connect(
                    self.update_status_dashboard)
                worker.signals.update_message.connect(
                    self.update_mesage_dashboard)
                worker.setAutoDelete(True)
                self.thead_pool.start(worker)

            except Exception as ex:
                self.update_mesage_dashboard(uid, f'{type(ex).__name__}: {ex}')

    def handle_seeding_action(self, uids, setting: SeedingSetting):
        sema_id = self.genarate_semaphore(setting.threads)
        if setting.auto_getlink:
            setting.posted_links = self.post_manager.get_post_approved_link()
        for uid in uids:
            try:
                account = self.account_manager.get_account_info(uid)
                if setting.auto_getlink:
                    liked_links = self.seeding_manager.get_seeding_liked_link(uid)
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
                self.thead_pool.start(worker)
            except Exception as ex:
                self.update_mesage_dashboard(uid, f'{type(ex).__name__}: {ex}')
                continue

    def on_update_seeding_status(self, uid, href, action):
        try:
            if action == 'Liked':
                self.post_manager.update_post_liked_counts(href)
            elif action == 'Commented':
                self.post_manager.update_post_commented_counts(href)

            self.seeding_manager.add_seeding_action(uid, href, action)
        except Exception as e:
            logging.error('', exc_info=True)

    def handle_check_group_allow_page(self, uid, group_links):
        sema_id = self.genarate_semaphore(1)
        try:
            account = self.account_manager.get_account_info(uid)

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
            self.thead_pool.start(worker)
        except Exception as e:
            logging.error('', exc_info=True)

    def on_update_allow_page_status(self, group_link, interact):
        try:
            self.group_tita_manager.update_group_interact(group_link, interact)
        except Exception as e:
            logging.error('', exc_info=True)

    def handle_check_approval_post(self, uid, pending_posts):
        sema_id = self.genarate_semaphore(1)
        try:
            account = self.account_manager.get_account_info(uid)

            worker = CheckApprovalPost(
                pending_posts, sema_id, account)
            worker.setAutoDelete(True)
            worker.signals.approved_post.connect(self.on_update_approve_status)

            #command signal
            worker.signals.update_status.connect(
                self.update_status_dashboard)
            worker.signals.update_message.connect(
                self.update_mesage_dashboard)
            self.thead_pool.start(worker)
            
        except Exception as ex:
            self.update_mesage_dashboard(uid, f'{type(ex).__name__}: {ex}')

    def on_update_approve_status(self, pending_post, status):
        try:
            self.post_manager.update_post_status(pending_post, status)
        except Exception as e:
            logging.error('', exc_info=True)

    def handle_scan_post_history(self, uids, loop_scan, sync_nick):
        sema_id = self.genarate_semaphore(sync_nick)
        for uid in uids:
            try:
                account = self.account_manager.get_account_info(uid)
                active_id = self.account_manager.get_account_pageid(uid)

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
                self.thead_pool.start(worker)
                
            except Exception as ex:
                self.update_mesage_dashboard(uid, f'{type(ex).__name__}: {ex}')

    def on_save_post_history(self, active_id, group_link, post_link, status):
        try:
            self.post_manager.add_post_history(
                active_id, group_link, post_link, status)
        except Exception as e:
            logging.error('', exc_info=True)

    def login_chrome(self, selected_uids):
        sema_id = self.genarate_semaphore(1)
        for uid in selected_uids:
            try:
                account = self.account_manager.get_account_info(uid)

                worker = LoginFacebookWorker(sema_id, account)
                worker.signals.update_status.connect(
                        self.update_status_dashboard)
                worker.signals.update_message.connect(
                        self.update_mesage_dashboard)
                worker.setAutoDelete(True)
                self.thead_pool.start(worker)

            except Exception as ex:
                self.update_mesage_dashboard(uid, f'{type(ex).__name__}: {ex}')

 

    def update_mesage_dashboard(self, uid, message):
        try:
            self.account_manager.update_account_message(uid, message)
            self.signals.update_dashboard.emit()
        except Exception as e:
            logging.error('', exc_info=True)

    def update_status_dashboard(self, uid, status):
        try:
            self.account_manager.update_account_status(uid, status)
            self.signals.update_dashboard.emit()
        except Exception as e:
            logging.error('', exc_info=True)

    def handle_scan_group_by_keyword(self, uid, keyword, loop_scan):
        sema_id = self.genarate_semaphore(1)
        try:
            account = self.account_manager.get_account_info(uid)

            worker = ScanGroupKeywordWorker(
                keyword, loop_scan, sema_id, account)
            worker.signals.update_status.connect(
                self.update_status_dashboard)
            worker.signals.update_message.connect(
                self.update_mesage_dashboard)
            worker.setAutoDelete(True)
            worker.signals.scan_keyword_completed.connect(
                self.scan_keyword_completed)
            self.thead_pool.start(worker)
        except Exception as ex:
            self.update_mesage_dashboard(uid, f'{type(ex).__name__}: {ex}')

    
    def scan_keyword_completed(self, uid, groups):
        talbe_name = 'groups_' + uid
        try:
            self.group_tita_manager.create_group_table(talbe_name)
            self.db_model._delete_all(talbe_name)
            request = InsertRequest(
                table=talbe_name,
                data= [asdict(group) for group in groups]
            )
            self.db_model.insert(request)
            
        except Exception as e:
            logging.error('', exc_info=True)

    def genarate_semaphore(self, resources):
        sema_id = uuid.uuid4()
        semaphore[sema_id] = QSemaphore(resources)
        return sema_id
