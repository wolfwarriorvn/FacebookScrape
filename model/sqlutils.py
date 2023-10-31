from PySide6 import QtWidgets, QtSql
from PySide6.QtSql import QSqlError
import logging

class SqlUtils:
    def __init__(self) -> None:
        super(SqlUtils, self).__init__()
        self.query = QtSql.QSqlQuery()
        # use this connection in Global
        # self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(r'H:\fbtools\fbdev.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS accounts (ID integer primary key, UserID VARCHAR(20) UNIQUE, Password VARCHAR(20), ProxyID VARCHAR(20))")
        self.query = QtSql.QSqlQuery()
        return True

    def excute(self, sql_query):
        self.query.prepare(sql_query)
        self.query.exec()

        if self.query.lastError().isValid():
            raise Exception(
                "SQL QUERY: {}\n".format(sql_query) +
                "ERROR INFO: {}".format(self.query.lastError().text())
            )
        
    def get_excute(self, sql_query):
        value = None
        self.query.prepare(sql_query)
        self.query.exec()

        while self.query.next():
            value = self.query.value(0)

        if self.query.lastError().isValid():
            raise Exception(
                "SQL QUERY: {}\n".format(sql_query) +
                "ERROR INFO: {}".format(self.query.lastError().text())
            )
        return value

    def get_excutes(self, sql_query):
        values = []
        self.query.prepare(sql_query)
        self.query.exec()

        while self.query.next():
            values.append(self.query.value(0))

        if self.query.lastError().isValid():
            raise Exception(
                "SQL QUERY: {}\n".format(sql_query) +
                "ERROR INFO: {}".format(self.query.lastError().text())
            )
        return values

    def delete_all_row(self, table_name):
        sql_query = "DELETE FROM {}".format(table_name)
        self.excute_query(sql_query, [])

    def create_groups_table(self, table_name):
        query = QtSql.QSqlQuery()
        sql_query = f"""CREATE TABLE IF NOT EXISTS {table_name} (ID integer primary key, Group_Link TEXT UNIQUE, Group_Name TEXT, Category TEXT, Numbers INTEGER, Details TEXT,Type TEXT, Status TEXT, Post_Time TEXT)"""
        query.prepare(sql_query)
        result = query.exec()
        if query.lastError().isValid():
            raise Exception(query.lastError().text())

    def create_new_table(self, table_name):
        query = QtSql.QSqlQuery()
        sql_query = f"""CREATE TABLE IF NOT EXISTS {table_name} (ID integer primary key, Group_Link VARCHAR(20) UNIQUE, Group_Name VARCHAR(20), PostedLink VARCHAR(100))"""
        query.prepare(sql_query)
        result = query.exec()
        if query.lastError().isValid():
            raise Exception(query.lastError().text())

    def excute_query(self, sql_query, values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if values is not None:
            for value in values:
                query.addBindValue(value)

        result = query.exec()
        if query.lastError().isValid():
            raise Exception(query.lastError().text(), query.lastQuery())

################ ACCOUNT QUERY####################


    def add_new_account_query(self, user_id, password, code2FA=None, email=None):
        sql_query = "INSERT INTO accounts ( UserID, Password, Code2FA, Email ) VALUES (?, ?, ?, ?)"
        self.excute_query(sql_query, [user_id, password, code2FA, email])

    def add_new_accounts_query(self, user_id, password, proxy_id):
        sql_query = "INSERT INTO accounts ( UserID, Password, ProxyID) VALUES (?, ?, ?)"
        self.excute_query(sql_query, [user_id, password, proxy_id])

    def update_account_query(self, id, user_id, password, proxy_id=None):
        sql_query = "UPDATE accounts SET UserID=?, Password=?, ProxyID=? WHERE ID=?"
        self.excute_query(sql_query, [user_id, password, proxy_id, id])

    def update_account_message(self, user_id, message):
        sql_query = "UPDATE accounts SET Message=? WHERE UserID=?"
        self.excute_query(sql_query, [message, user_id])

    def update_account_status(self, user_id, status):
        sql_query = "UPDATE accounts SET Status=? WHERE UserID=?"
        self.excute_query(sql_query, [status, user_id])

    def delete_accounts(self, id):
        sql_query = "DELETE FROM accounts WHERE ID BETWEEN 4 AND 7"
        self.excute_query(sql_query, [id])

    def get_accounts(self, id):
        query = QtSql.QSqlQuery()
        UserID, Password, ProxyID, _2FA, Cookie, Email, PassEmail = range(7)
        sql_query = f"""SELECT UserID, Password, ProxyID, Code2FA, Cookie, Email, PassEmail FROM accounts WHERE UserID={id}"""
        query.prepare(sql_query)
        query.exec()
        while query.next():
            return [    query.value(UserID),
                        query.value(Password), 
                        query.value(ProxyID),
                        query.value(_2FA),
                        query.value(Cookie),
                        query.value(Email),
                        query.value(PassEmail)]

        if query.lastError().isValid():
            raise Exception(query.lastError().text(), sql_query)
        return []

    def get_approved_post(self):
        sql_query = "SELECT Post_Link FROM posts WHERE Status='Approved'"
        self.query.prepare(sql_query)
        self.query.exec()
        while self.query.next():
            return self.query.value(0)

        if self.query.lastError().isValid():
            raise Exception(self.query.lastError().text())
        return []

    def update_mul_proxy(self, proxy, list_id):
        sql_query = "UPDATE accounts SET ProxyID={} ({})".format(proxy,
                                                                 ",".join(['?' for id in list_id]))
        self.excute_query(sql_query, list_id)

    def delete_mul_accounts(self, list_id):
        sql_query = "DELETE FROM accounts WHERE ID IN ({})".format(
            ",".join(['?' for id in list_id]))
        self.excute_query(sql_query, list_id)

    ################ PROXY QUERY###################
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
            return query.value(0)
        return None

    def delete_mul_groups(self, page_tb, group_link):
        sql_query = "DELETE FROM {} WHERE Group_Link IN ({})".format(page_tb,
                                                                     ",".join(['?' for id in group_link]))
        self.excute_query(sql_query, group_link)

    def get_group_query(self, page_tb):
        groups = []
        query = QtSql.QSqlQuery()
        sql_query = f"""SELECT Group_Link FROM {page_tb}"""
        query.prepare(sql_query)
        query.exec()
        while query.next():
            groups.append(query.value(0))
        return groups

    def add_groups(self, table, groups):
        query = QtSql.QSqlQuery()
        sql_query = "INSERT INTO {} (Group_Link, Group_Name, Category, Numbers, Details) VALUES {}".format(table,
                                                                                                           ",".join(['(?,?,?,?,?)' for id in groups]))
        query.prepare(sql_query)
        for group in groups:
            query.addBindValue(group.link)
            query.addBindValue(group.name)
            query.addBindValue(group.category)
            query.addBindValue(group.members)
            query.addBindValue(group.details)
        result = query.exec()
        if query.lastError().isValid():
            raise Exception(query.lastError().text())

    def add_group_query(self, page_tb, groups):
        query = QtSql.QSqlQuery()
        sql_query = "INSERT INTO {} (Group_Link, Group_Name) VALUES {}".format(page_tb,
                                                                               ",".join(['(?,?)' for id in groups]))
        query.prepare(sql_query)
        for group in groups:
            query.addBindValue(group.link)
            query.addBindValue(group.name)
        result = query.exec()
        if query.lastError().isValid():
            raise Exception(query.lastError().text())
