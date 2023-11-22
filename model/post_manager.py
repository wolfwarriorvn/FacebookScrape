from model.request import SelectRequest, InsertRequest, DeleteRequest, UpdateRequest
from model.db_model import DatabaseModel
from datetime import datetime


class PostManager:
    def __init__(self, db_model: DatabaseModel) -> None:
        self.db_model = db_model
        self.table_name = 'posts'

    def update_post_status(self, pending_post, status):
        update_request = UpdateRequest(
            table=self.table_name,
            data={'Status': status},
            conditions="Post_Link = :pending_post",
            parameters={'pending_post': pending_post}
        )
        self.db_model.update(update_request)

    def update_post_commented_counts(self, link):
        update_request = UpdateRequest(
            table=self.table_name,
            expressions={'Commented': 'Commented + 1'},
            conditions="Post_Link = :link",
            parameters={'link': link}
        )
        self.db_model.update(update_request)

    def update_post_liked_counts(self, link):
        update_request = UpdateRequest(
            table=self.table_name,
            expressions={'Liked': 'Liked + 1'},
            conditions="Post_Link = :link",
            parameters={'link': link}
        )
        self.db_model.update(update_request)

    def get_post_approved_link(self):
        select_request = SelectRequest(
            table=self.table_name,
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
            table=self.table_name,
            data=history_data
        )
        self.db_model.insert(insert_request)
