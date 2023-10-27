from PySide6.QtCore import QObject
from PySide6.QtCore import Signal, Slot
from PySide6.QtCore import QThreadPool, QSemaphore

from model.model import Model

from controllers.worker import *
from common.payload import *

import uuid
import random
from controllers.worker.base_worker import semaphore


class AccountInfo:
    def __init__(self, uid, pw, proxy) -> None:
        self.uid = uid
        self.pw = pw
        self.proxy = proxy


class MySignals(QObject):
    # Edit account signal
    table_on_load = Signal()
    get_account_completed = Signal(object)
    save_account_completed = Signal()
    create_table_db = Signal(str)
    update_dashboard = Signal()

    wrong_user_input = Signal()
    table_get_completed = Signal(object)
    add_user_completed = Signal()
    add_user_error = Signal(object)

    # Pages Manage
    get_accounts = Signal()
    get_accounts_completed = Signal(object)

    # facebook
    post_event = Signal(object, object)
    scan_joined_group = Signal(object, object)
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

class DbSignals(QObject):
    # Proxy table
    proxy_add = Signal(str, str)
    proxy_add_completed = Signal()
    proxy_detete = Signal(object)
    get_free_group = Signal(str)
    get_free_group_completed = Signal(int)
    #account table
    account_add = Signal(str, str, str)
    account_add_response = Signal()

class MainController(QObject):
    # sg_wrong_user_input = Signal()
    signals = MySignals()
    db_signals = DbSignals()

    def __init__(self, model: Model):
        super().__init__()
        self.pool = QThreadPool.globalInstance()
        self._model = model
        self.signals.table_on_load.connect(self.update_table_view)

        self.signals.get_accounts.connect(self.on_get_accounts)
        self.signals.checkpoint_956.connect(self.init_thread_checkpoint_956)
        self.signals.create_table_db.connect(self.create_table)
        self.signals.check_approval_post.connect(
            self.init_thread_check_approval_post)
        self.signals.check_group_allow_page.connect(
            self.init_thread_check_group_allow_page)

        self.signals.scan_joined_group.connect(self.scan_joined_group)
        self.signals.post_event.connect(self.init_thread_post)
        self.signals.scan_group_by_keyword.connect(self.scan_group_by_keyword)
        self.signals.scan_post_history.connect(self.on_scan_post_history)
        self.signals.seeding_action.connect(self.init_thread_seeding_action)
        self.db_signals.get_free_group.connect(self.on_get_free_group)
        self.db_signals.proxy_add.connect(self.on_add_proxy)
        self.db_signals.account_add.connect(self.on_account_add)

    def on_account_add(self, input_accounts, category, acc_format):
        accs_raw = input_accounts.splitlines()
        try:
            for acc in accs_raw:
                elements = acc.split('|')
                if acc_format in AccountFormat.UID_PASS:
                    uid, pwd = acc.split('|')
                    self._model.add_account_info(uid, pwd)
                    self.signals.add_user_completed.emit()

                elif acc_format in AccountFormat.CUSTOM1:
                    uid, pwd, code2fa, email, pass_email, cookie, token, birthday, *stuff = acc.split('|')
                    self._model.add_account_info(uid, pwd, category, code2fa, cookie, token,email, pass_email , birthday)
                    self.signals.add_user_completed.emit()

                elif acc_format in AccountFormat.CUSTOM2:
                    uid, pwd, code2fa, cookie, token,email, pass_email , birthday, *stuff = acc.split('|')
                    self._model.add_account_info(uid, pwd, category, code2fa, cookie, token,email, pass_email , birthday)
                    self.signals.add_user_completed.emit()

                elif acc_format in AccountFormat.DUYAN_5K:
                    uid, pwd, code2fa, email, pass_email, _, birthday, cookie, token, *stuff = acc.split('|')
                    self._model.add_account_info(uid, pwd, category, code2fa, cookie, token,email, pass_email , birthday)
                    self.signals.add_user_completed.emit()
                else:
                    print("Input khong dung format")
                    self.signals.add_user_error.emit()

        except Exception as e:
            # print("Error is {}".format(e))
            self.signals.add_user_error.emit(e)

    def on_get_free_group(self, type_groups):
        free_group_links = self._model.get_group_free(type_groups)
        self.db_signals.get_free_group_completed.emit(len(free_group_links))

    def on_add_proxy(self, proxy, proxy_zip):
        try:
            self._model.add_proxy(proxy, proxy_zip)
            self.db_signals.proxy_add_completed.emit()
        except Exception as e:
            print("create_table error: ", e)
            pass

    def init_thread_post(self, uids, setting: PostSetting):
        sema_id = self.genarate_semaphore(setting.threads)
        free_group_links = self._model.get_group_free(setting.type_group)
        total_post = len(uids) * setting.post_count
        if total_post > len(free_group_links):
            print("Emit hết nick nha")
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
            print("post_completed error", e)
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
                liked_links = self._model.get_seeding_liked_link(uid)
                account = self._model.get_account_info(uid)

                set_available_links = set(
                    setting.posted_links).difference(set(liked_links))
                if len(set_available_links) < setting.seedings:
                    self.update_mesage_dashboard(
                        uid, 'Không đủ link để like. Số link còn lại: {}'.format(len(set_available_links)))
                    continue

                available_links = random.sample(
                    sorted(set_available_links), setting.seedings)

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
            print("on_update_allow_page_status: ", e)
            pass

    def init_thread_check_group_allow_page(self, uid, group_links):
        sema_id = self.genarate_semaphore(1)
        try:
            account = self._model.get_account_info(uid)

            worker = CheckGroupAllowPage(
                group_links, account)
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
            print("create_table error: ", e)
            pass

    def on_update_allow_page_status(self, group_link, interact):
        try:
            self._model.update_group_interact(group_link, interact)
        except Exception as e:
            print("on_update_allow_page_status: ", e)
            pass

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
            print("on_update_approve_status: ", e)
            pass

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
            pass

    def on_get_accounts(self):
        accounts = self._model.get_account_userids()
        self.signals.get_accounts_completed.emit(accounts)

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
            print("create_table error: ", e)
            pass

    def update_status_dashboard(self, uid, status):
        try:
            self._model.update_account_status(uid, status)
            self.signals.update_dashboard.emit()
        except Exception as e:
            print("create_table error: ", e)
            pass

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
            print("save group data failed: ", e)
            pass

    Slot(object, object)

    def scan_joined_group(self, uids, page_ids):
        sema_id = self.genarate_semaphore(1)
        try:
            for idx_uid, idx_page_id in zip(uids, page_ids):
                account = self._model.get_account_info(idx_uid)

                worker = ScanJoinedGroupWorker(
                    idx_page_id, sema_id, account)
                worker.setAutoDelete(True)
                worker.signals.scan_complted.connect(self.scan_completed)
                self.pool.start(worker)
        except Exception as ex:
            self.update_mesage_dashboard(uid, f'{type(ex).__name__}: {ex}')

    def scan_completed(self, activeID, group_list):
        talbe_name = 'groups_' + activeID
        try:
            self._model.create_table(talbe_name)
            self._model.add_group(talbe_name,
                                  group_list)
            self.signals.scan_group_completed.emit()
        except Exception as e:
            print("save group data failed: ", e)
            pass

    Slot(str)
    def create_table(self, talbe_name):
        try:
            self._model.create_table(talbe_name)
        except Exception as e:
            print("create_table error: ", e)
            pass
    Slot(str)
    def get_account_info(self, indexs):
        try:
            if len(indexs) == 1:
                uid, pw, proxy = self._model.get_account_info(indexs[0])
                self.signals.get_account_completed.emit(
                    AccountInfo(uid, pw, proxy))
        except Exception as e:
            print("create_table error: ", e)
            pass

    Slot(str)
    def add_new_account(self, raw_input):
        accs_raw = raw_input.splitlines()
        try:
            for acc in accs_raw:
                lenght_elements = acc.split('|')

                if acc in AccountFormat.UID_PASS:
                    uid, pwd = acc.split('|')
                    self._model.add_account_info(uid, pwd)
                    self.signals.add_user_completed.emit()
                elif len(acc.split('|')) == 3:
                    uid, pwd, code2fa = acc.split('|')
                    self._model.add_account_info(uid, pwd, code2fa)
                    self.signals.add_user_completed.emit()
                elif len(acc.split('|')) == 5:
                    uid, pwd, code2fa, email, _pass_email = acc.split('|')
                    self._model.add_account_info(
                        uid, pwd, code2fa, '{}|{}'.format(email, _pass_email))
                    self.signals.add_user_completed.emit()
                else:
                    print("Input khong dung format")
                    self.signals.add_user_error.emit()

        except Exception as e:
            print("Error is {}".format(e))
            self.signals.add_user_error.emit()

    Slot()

    def update_table_view(self):
        self.signals.table_get_completed.emit(self._model._get_table())

    Slot(object, list)

    def delete_account(self, tb_model, acc_index):
        ids = []
        for index in sorted(acc_index):
            id = str(tb_model.data(index))
            ids.append(id)
        self._model.delete_account(ids)
        self.signals.table_get_completed.emit(self._model._get_table())

    def genarate_semaphore(self, resources):
        sema_id = uuid.uuid4()
        semaphore[sema_id] = QSemaphore(resources)
        return sema_id
