from PySide6 import QtWidgets, QtSql

class Database:
    def __init__(self):
        super(Database, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(r'H:\fbtools\fbscrape.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS accounts (ID integer primary key, UserID VARCHAR(20) UNIQUE, Password VARCHAR(20), ProxyID integer)")

        query.exec("CREATE TABLE IF NOT EXISTS groups_tita (ID integer primary key, Group_Link TEXT UNIQUE, Group_Name TEXT, Category TEXT, Numbers INTEGER, Details TEXT, Type TEXT, Status TEXT, Post_Time TEXT)")

        query.exec("CREATE TABLE IF NOT EXISTS posts (ID integer primary key, PageID TEXT, Group_Link TEXT, Post_Time TEXT, Href TEXT, Posted_Link TEXT, Note TEXT)")

        query.exec("CREATE TABLE IF NOT EXISTS seedings (ID integer primary key, UserID TEXT, Poste_Link TEXT, Action TEXT, TIME TEXT)")
        return True