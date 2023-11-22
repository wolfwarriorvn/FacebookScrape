from model.request import SelectRequest, InsertRequest, DeleteRequest, UpdateRequest
from model.db_model import DatabaseModel


class ProxyManager:
    def __init__(self, db_model: DatabaseModel) -> None:
        self.db_model = db_model
        self.table_name = 'proxy'

    def get_proxy_extension(self, id):
        if not id:
            return None
        select_request = SelectRequest(
            table=self.table_name,
            columns='zip_proxy',
            conditions="ID=:id",
            parameters={'id': id})
        proxy_extension = self.db_model.select(select_request)

        return proxy_extension[0].get('zip_proxy', None) if proxy_extension else None
