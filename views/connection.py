from PySide6 import QtWidgets, QtSql

class Connection:
    def __init__(self) -> None:
        super(Connection, self).__init__()

    def excute_query(self, sql_query, values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)
        
        if values is not None:
            for value in values:
                query.addBindValue(value)

        query.exec()

    def add_new_account_query(self, user_id, password, proxy_id):
        sql_query = "INSERT INTO accounts ( UserID, Password, ProxyID) VALUES (?, ?, ?)"
        self.excute_query(sql_query, [user_id, password, proxy_id])

