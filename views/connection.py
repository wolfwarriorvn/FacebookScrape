from PySide6 import QtWidgets, QtSql

class Connection:
    def __init__(self) -> None:
        super(Connection, self).__init__()
        #use this connection in Global
        # self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('fbscrape.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS expenses (ID integer primary key AUTOINCREMENT, Date VARCHAR(20), "
                   "Category VARCHAR(20), Description VARCHAR(20), Balance REAL, Status VARCHAR(20))")
        return True

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

