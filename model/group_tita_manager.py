from model.request import SelectRequest, InsertRequest, DeleteRequest, UpdateRequest
from model.db_model import DatabaseModel
from datetime import datetime


class GroupTitaManager:
    def __init__(self, db_model: DatabaseModel) -> None:
        self.db_model = db_model
        TABLE_NAME = 'accounts'
        self.table_name = 'groups_tita'


    def create_group_table(self, table_name):
        if table_name is None:
            raise ValueError('Table name is required!')
        
        query = f"""CREATE TABLE IF NOT EXISTS {table_name} (ID integer primary key, Group_Link TEXT UNIQUE, Group_Name TEXT, Category TEXT, Numbers INTEGER, Details TEXT,Type TEXT, Status TEXT, Post_Time TEXT)"""

        self.db_model.execute_sql_query(query)

    def update_group_interact(self, link, interact):
        update_request = UpdateRequest(
            table=self.table_name,
            data={'Interact': interact},
            conditions="Group_Link = :link",
            parameters={'link': link}
        )
        self.db_model.update(update_request)

    def update_group_posted_status(self, pageid, link, status):
        update_request = UpdateRequest(
            table=self.table_name,
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
            table=self.table_name,
            columns='Group_Link',
            conditions="Type = :type and Category='Công khai ' and Interact='Page' and (Status IS NULL or Status = 'Free')",
            parameters={'type': group_type})

        groups = self.db_model.select(SelectRequest)
        return [entry.get('Group_Link') for entry in groups]
