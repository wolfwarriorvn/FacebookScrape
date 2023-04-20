from PySide6 import QtWidgets, QtSql

class Database:
    def __init__(self):
        super(Database, self).__init__()
        self.create_connection()

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