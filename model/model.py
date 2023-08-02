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

    def add_new_account(self, uid, pwd, proxy_id=None):
        self.sql_utils.add_new_account_query(uid, pwd, proxy_id)
    
    def get_account_info(self, id):
        return self.sql_utils.get_accounts(id)

    def save_account_info(self, id, account_info):
        self.sql_utils.update_account_query(id, account_info.uid, account_info.pw, account_info.proxy)

    def delete_account(self, id):
        self.sql_utils.delete_mul_accounts(id)

    def add_proxy(self, proxy, proxy_zip):
        self.sql_utils.add_proxy_query(proxy, proxy_zip)

    def get_proxy_extension(self, id):
        return self.sql_utils.get_proxy_extension(id)