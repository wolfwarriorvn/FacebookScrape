from model.request import SelectRequest, InsertRequest, DeleteRequest, UpdateRequest
from model.db_model import DatabaseModel
from model.db_model import AccountInfo
from dataclasses import dataclass, asdict
from model.proxy_namager import ProxyManager


class AccountManager:
    TABLE_NAME = 'accounts'

    def __init__(self, db_model: DatabaseModel) -> None:
        self.db_model = db_model

    def create_table(self, table_name):
        if table_name is None:
            raise ValueError('Table name is required!')

        query = f"""CREATE TABLE IF NOT EXISTS {table_name} (ID integer primary key, Group_Link TEXT UNIQUE, Group_Name TEXT, Category TEXT, Numbers INTEGER, Details TEXT,Type TEXT, Status TEXT, Post_Time TEXT)"""
        
        self.db_model.execute_sql_query(query)

    def get_account_info(self, uid):
        select_request = SelectRequest(
            table=self.TABLE_NAME,
            conditions="UserID = :userid",
            parameters={'userid': uid}
        )
        ret_account = self.db_model.select(select_request)

        if len(ret_account) != 1:
            raise Exception("Can't find user ID")
        account = ret_account[0]

        proxy_extension = ProxyManager(self.db_model).get_proxy_extension(
            account.get('ProxyID', None))

        return AccountInfo(
            account['UserID'],
            account['Password'],
            proxy_extension,
            account['Code2FA'],
            account['Cookie'],
            account['Email'],
            account['PassEmail'],
        )

    def get_account_pageid(self, uid):
        select_request = SelectRequest(
            table=self.TABLE_NAME,
            columns='PageID',
            conditions="UserID=:userid",
            parameters={'userid': uid})

        pageid = self.db_model.select(select_request)
        return pageid[0].get('PageID', None) if pageid else None

    def update_account_status(self, uid, status):
        update_request = UpdateRequest(
            table=self.TABLE_NAME,
            data={'Status': status},
            conditions="UserID = :userid",
            parameters={'userid': uid}
        )
        self.db_model.update(update_request)

    def update_account_message(self, uid, message):
        update_request = UpdateRequest(
            table=self.TABLE_NAME,
            data={'Message': message},
            conditions="UserID = :userid",
            parameters={'userid': uid}
        )
        self.db_model.update(update_request)
