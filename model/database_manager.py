from model.db_model import DatabaseModel
from model.request import SelectRequest, InsertRequest, DeleteRequest, UpdateRequest
from model.db_model import AccountInfo
from datetime import datetime
from dataclasses import dataclass, asdict


class Table:
    ACCOUNTS = 'accounts'
    GROUP_TITA = 'groups_tita'
    POSTS = 'posts'
    PROXY = 'proxy'
    SEEDING = 'seedings'
    APPROVE_REQUEST = 'approve_request'


class DatabaseManager:
    def __init__(self, db_model: DatabaseModel) -> None:
        self.db_model = db_model

    def get_proxy_extension(self, id):
        if not id:
            return None
        select_request = SelectRequest(
            table=Table.PROXY,
            columns='zip_proxy',
            conditions="ID=:id",
            parameters={'id': id})
        proxy_extension = self.db_model.select(select_request)

        return proxy_extension[0].get('zip_proxy', None) if proxy_extension else None

    def get_account_info(self, uid):
        select_request = SelectRequest(
            table=Table.ACCOUNTS,
            conditions="UserID = :userid",
            parameters={'userid': uid}
        )
        ret_account = self.db_model.select(select_request)

        if len(ret_account) != 1:
            raise Exception("Can't find user ID")
        account = ret_account[0]

        proxy_extension = self.get_proxy_extension(
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
            table=Table.ACCOUNTS,
            columns='PageID',
            conditions="UserID=:userid",
            parameters={'userid': uid})

        pageid = self.db_model.select(select_request)
        return pageid[0].get('PageID', None) if pageid else None

    def update_account_status(self, uid, status):
        update_request = UpdateRequest(
            table=Table.ACCOUNTS,
            data={'Status': status},
            conditions="UserID = :userid",
            parameters={'userid': uid}
        )
        self.db_model.update(update_request)

    def update_account_message(self, uid, message):
        update_request = UpdateRequest(
            table=Table.ACCOUNTS,
            data={'Message': message},
            conditions="UserID = :userid",
            parameters={'userid': uid}
        )
        self.db_model.update(update_request)

    def get_seeding_liked_link(self, uid):
        select_request = SelectRequest(
            table=Table.SEEDING,
            columns='Post_Link',
            conditions="Action='Liked' and UserID=:userid",
            parameters={'userid': uid})
        groups = self.db_model.select(select_request)
        return [entry.get('Post_Link') for entry in groups]

    def add_seeding_action(self, uid, link, action):
        seedings_data = [{
            'UserID': uid,
            'Post_Link': link,
            'Action': action,
            'TIME': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }]
        insert_request = InsertRequest(
            table=Table.SEEDING,
            data=seedings_data
        )
        self.db_model.insert(insert_request)

    def update_post_status(self, pending_post, status):
        update_request = UpdateRequest(
            table=Table.POSTS,
            data={'Status': status},
            conditions="Post_Link = :pending_post",
            parameters={'pending_post': pending_post}
        )
        self.db_model.update(update_request)

    def update_post_commented_counts(self, link):
        update_request = UpdateRequest(
            table=Table.POSTS,
            expressions={'Commented': 'Commented + 1'},
            conditions="Post_Link = :link",
            parameters={'link': link}
        )
        self.db_model.update(update_request)

    def update_post_liked_counts(self, link):
        update_request = UpdateRequest(
            table=Table.POSTS,
            expressions={'Liked': 'Liked + 1'},
            conditions="Post_Link = :link",
            parameters={'link': link}
        )
        self.db_model.update(update_request)

    def get_post_approved_link(self):
        select_request = SelectRequest(
            table=Table.POSTS,
            columns='Post_Link',
            conditions="Status = :status",
            parameters={'status': 'Approved'})
        groups = self.db_model.select(select_request)
        return [entry.get('Post_Link') for entry in groups]

    def add_post_history(self, active_id, group_link, post_link, status):
        history_data = [{
            'UserID': active_id,
            'Group_Link': group_link,
            'Post_Link': post_link,
            'Status': status,
            'TIME': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }]
        insert_request = InsertRequest(
            table=Table.POSTS,
            data=history_data
        )
        self.db_model.insert(insert_request)

    def create_group_table(self, table_name):
        if table_name is None:
            raise ValueError('Table name is required!')

        query = f"""CREATE TABLE IF NOT EXISTS {table_name} (ID integer primary key, Group_Link TEXT UNIQUE, Group_Name TEXT, Category TEXT, Numbers INTEGER, Details TEXT,Type TEXT, Status TEXT, Post_Time TEXT)"""

        self.db_model.execute_sql_query(query)

    def save_scanned_groups_table(self, table_name, groups):
        self.create_group_table(table_name)
        self.db_model._delete_all(table_name)

        request = InsertRequest(
                table=table_name,
                data= [asdict(group) for group in groups]
            )
        self.db_model.insert(request)

    def update_group_interact(self, link, interact):
        update_request = UpdateRequest(
            table=Table.GROUP_TITA,
            data={'Interact': interact},
            conditions="Group_Link = :link",
            parameters={'link': link}
        )
        self.db_model.update(update_request)

    def update_group_posted_status(self, pageid, link, status):
        update_request = UpdateRequest(
            table=Table.GROUP_TITA,
            data={
                'Status': status,
                'Post_Time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'Posted_Page': pageid
            },
            conditions="Group_Link = :link",
            parameters={'link': link}
        )
        self.db_model.update(update_request)

    def get_group_free(self, group_type):
        select_quest = SelectRequest(
            table=Table.GROUP_TITA,
            columns='Group_Link',
            conditions="Type = :type and Category='Công khai ' and Interact='Page' and (Status IS NULL or Status = 'Free')",
            parameters={'type': group_type})

        groups = self.db_model.select(SelectRequest)
        return [entry.get('Group_Link') for entry in groups]
    
    def add_approve_request(self, aprove_requests):
        request = InsertRequest(
                table=Table.APPROVE_REQUEST,
                data= [asdict(entry) for entry  in aprove_requests]
            )
        self.db_model.insert(request)
