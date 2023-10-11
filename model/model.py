from PySide6.QtCore import QObject
from PySide6.QtSql import QSqlTableModel
from model.sqlutils import SqlUtils


class Model(QObject):
    def __init__(self):
        super().__init__()
        self._tb_model = QSqlTableModel(self)
        self.sql_utils = SqlUtils()

    def _get_table(self):
        self._tb_model.setTable('accounts')
        self._tb_model.select()
        return self._tb_model

    def create_table(self, table_name):
        self.sql_utils.create_new_table(table_name)

    def create_group_table(self, table_name):
        self.sql_utils.create_groups_table(table_name)

    def get_account_info(self, uid):
        return self.sql_utils.get_accounts(uid)

    def get_account_userids(self):
        sql_query = f"""SELECT UserID FROM accounts"""
        return self.sql_utils.get_excutes(sql_query)

    def get_account_2fa(self, uid):
        sql_query = f"""SELECT Code2FA FROM accounts WHERE UserID='{uid}'"""
        return self.sql_utils.get_excute(sql_query)

    def get_account_pageid(self, uid):
        sql_query = f"""SELECT PageID FROM accounts WHERE UserID='{uid}'"""
        return self.sql_utils.get_excute(sql_query)

    def add_account_info(self, uid, pwd, code2FA=None, email=None):
        sql_query = f"""INSERT INTO accounts ( UserID, Password, Code2FA, Email ) VALUES ({uid}, '{pwd}', '{code2FA}', '{email}')"""
        self.sql_utils.excute(sql_query)

    def update_account_message(self, uid, message):
        sql_query = f"""UPDATE accounts SET Message='{message}' WHERE UserID='{uid}'"""
        self.sql_utils.excute(sql_query)

    def update_account_status(self, uid, status):
        sql_query = f"""UPDATE accounts SET Status='{status}' WHERE UserID='{uid}'"""
        self.sql_utils.excute(sql_query)

    def get_group_free(self, _type):
        sql_query = f"""SELECT Group_Link FROM groups_tita WHERE Type = '{_type}' and Category='Công khai ' and Interact='Page' and (Status IS NULL or Status = 'Free')"""
        return self.sql_utils.get_excutes(sql_query)

    def update_group_interact(self, link, interact):
        sql_query = f"""UPDATE groups_tita SET Interact='{interact}' WHERE Group_Link='{link}'"""
        self.sql_utils.excute(sql_query)

    def add_seeding_action(self, uid, link, action):
        sql_query = f"""INSERT INTO seedings (UserID, Post_Link, Action, TIME) VALUES ('{uid}', '{link}', '{action}', datetime('now','localtime'))"""
        self.sql_utils.excute(sql_query)

    def update_post_liked_counts(self, link):
        sql_query = f"""UPDATE posts SET Liked=Liked+1 WHERE Post_Link='{link}'"""
        self.sql_utils.excute(sql_query)

    def update_post_commented_counts(self, link):
        sql_query = f"""UPDATE posts SET Commented=Commented+1 WHERE Post_Link='{link}'"""
        self.sql_utils.excute(sql_query)

    def get_post_approved_link(self):
        sql_query = "SELECT Post_Link FROM posts WHERE Status='Approved'"
        return self.sql_utils.get_excutes(sql_query)

    def get_seeding_liked_link(self, uid):
        sql_query = f"""SELECT Post_Link FROM seedings WHERE Action='Liked' and UserID='{uid}'"""
        return self.sql_utils.get_excutes(sql_query)

    def update_post_status(self, pending_post, status):
        sql_query = f"""UPDATE posts SET Status='{status}' WHERE Post_Link='{pending_post}'"""
        self.sql_utils.excute(sql_query)

    def add_post_history(self, active_id, group_link, post_link, status):
        sql_query = f"""INSERT INTO posts (UserID, Group_Link, Post_Link, Status,Time) VALUES ('{active_id}', '{group_link}', '{post_link}', '{status}', datetime('now','localtime'))"""
        self.sql_utils.excute(sql_query)

    def update_group_posted_status(self, pageid, link, status):
        sql_query = f"""UPDATE groups_tita SET Status='{status}', Post_Time=datetime('now','localtime'), Posted_Page='{pageid}' WHERE Group_Link='{link}'"""
        self.sql_utils.excute(sql_query)

    def delete_account(self, id):
        self.sql_utils.delete_mul_accounts(id)

    def add_proxy(self, proxy, proxy_zip):
        sql_query = "INSERT INTO proxy (ProxyID, zip_proxy) VALUES ('{}','{}')".format(
            proxy, proxy_zip)
        self.sql_utils.excute(sql_query)

    def get_proxy_extension(self, id):
        if id == '':
            return None
        sql_query = f"""SELECT zip_proxy FROM proxy WHERE ID={id}"""
        return self.sql_utils.get_excute(sql_query)

    def add_group_scan(self, table, groups):
        self.sql_utils.delete_all_row(table)
        self.sql_utils.add_groups(table, groups)

    def add_group(self, tb_groups, groups):
        new_groups = []
        group_link = self.sql_utils.get_group_query(tb_groups)
        # check new group
        for idx, x in enumerate(groups):
            if x.link not in group_link:
                new_groups.append(x)

        # check out group
        all_scan_links = [i.link for i in groups]
        del_groups = []
        for save_link in group_link:
            if save_link not in all_scan_links:
                del_groups.append(save_link)
        if del_groups:
            self.sql_utils.delete_mul_groups(tb_groups, del_groups)

        if new_groups:
            self.sql_utils.add_group_query(tb_groups, new_groups)
