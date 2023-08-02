from PySide6 import QtWidgets, QtSql
from PySide6.QtSql import QSqlError


class SqlUtils:
    def __init__(self) -> None:
        super(SqlUtils, self).__init__()
        # use this connection in Global
        # self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('fbscrape.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS accounts (ID integer primary key, UserID VARCHAR(20) UNIQUE, Password VARCHAR(20), ProxyID VARCHAR(20))")
        return True

    def excute_query(self, sql_query, values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if values is not None:
            for value in values:
                query.addBindValue(value)

        result = query.exec()
        if query.lastError().isValid():
            raise Exception(query.lastError().text())
            print(query.lastError().type())
            print(query.lastError().text())
            # print(query.lastError())


    def add_new_account_query(self, user_id, password, proxy_id=None):
        sql_query = "INSERT INTO accounts ( UserID, Password, ProxyID) VALUES (?, ?, ?)"
        self.excute_query(sql_query, [user_id, password, proxy_id])

    def add_new_accounts_query(self, user_id, password, proxy_id):
        sql_query = "INSERT INTO accounts ( UserID, Password, ProxyID) VALUES (?, ?, ?)"
        self.excute_query(sql_query, [user_id, password, proxy_id])

    def update_account_query(self, id, user_id, password, proxy_id=None):
        sql_query = "UPDATE accounts SET UserID=?, Password=?, ProxyID=? WHERE ID=?"
        self.excute_query(sql_query, [user_id, password, proxy_id, id])
        

    def delete_accounts(self, id):
        sql_query = "DELETE FROM accounts WHERE ID BETWEEN 4 AND 7"
        self.excute_query(sql_query, [id])
    
    def get_accounts(self, id):
        query = QtSql.QSqlQuery()
        UserID, Password, ProxyID = range(3)
        sql_query = f"""SELECT UserID, Password, ProxyID FROM accounts WHERE ID={id}"""
        query.prepare(sql_query)
        query.exec()
        while query.next():
            return [query.value(UserID),query.value(Password),query.value(ProxyID)]
        return []

    def update_mul_proxy(self, proxy, list_id):
        sql_query = "UPDATE accounts SET ProxyID={} ({})".format(proxy,
            ",".join(['?' for id in list_id]))
        self.excute_query(sql_query, list_id)

    def delete_mul_accounts(self, list_id):
        sql_query = "DELETE FROM accounts WHERE ID IN ({})".format(
            ",".join(['?' for id in list_id]))
        self.excute_query(sql_query, list_id)

    ################PROXY QUERY####################
    def add_proxy_query(self, proxy, zip_proxy):
        sql_query = "INSERT INTO proxy (ProxyID, zip_proxy) VALUES (?, ?)"
        self.excute_query(sql_query, [proxy, zip_proxy])

    def delete_mul_proxy(self, proxy):
        sql_query = "DELETE FROM proxy WHERE ID IN ({})".format(
            ",".join(['?' for id in proxy]))
        self.excute_query(sql_query, proxy)
    def get_proxy_extension(self, id):
        query = QtSql.QSqlQuery()
        sql_query = f"""SELECT zip_proxy FROM proxy WHERE ID={id}"""
        query.prepare(sql_query)
        query.exec()
        while query.next():
            print("data return: ", query.value(0))
            return query.value(0)
        return None
# util = SqlUtils()
# # # util.add_new_account_query('123', '1123', '123213')
# # util.update_account_query('1', 'fuck', 'nha')
# print(util.get_accounts(1))