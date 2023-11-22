from model.request import SelectRequest, InsertRequest, DeleteRequest, UpdateRequest
from model.db_model import DatabaseModel
from datetime import datetime


class SeedingManager:
    def __init__(self, db_model: DatabaseModel) -> None:
        self.db_model = db_model
        self.table_name = 'seedings'

    def get_seeding_liked_link(self, uid):
        select_request = SelectRequest(
            table=self.table_name,
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
            table=self.table_name,
            data=seedings_data
        )
        self.db_model.insert(insert_request)
