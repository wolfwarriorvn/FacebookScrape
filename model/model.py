from PySide6.QtCore import QObject
from PySide6.QtSql import QSqlTableModel, QSqlQuery, QSqlDatabase
from controllers.request import *
from datetime import datetime
from setting import main_setting
from dataclasses import dataclass, asdict
from common.payload import UserAccount


class AccountInfo():
    def __init__(self, uid, password, proxy, secret_2fa, cookie, email, pass_email) -> None:
        self.uid = uid
        self.password = password
        self.proxy = proxy
        self.secret_2fa = secret_2fa
        self.cookie = cookie
        self.email = email
        self.pass_email = pass_email

class DatabaseModel(QObject):
    def __init__(self):
        super().__init__()
        self.database = QSqlDatabase.addDatabase('QSQLITE')
        self.database.setDatabaseName(main_setting.database)

        if not self.database.open():
            raise Exception("Error: Unable to open the database connection.")

    
    def execute_sql_query(self, query_text, parameters=None):
        """
        Executes an SQL query using the provided parameters.

        :param query_text: The SQL query string with placeholders.
        :param parameters: A dictionary where keys correspond to placeholders in the query.
        """
        query = QSqlQuery()
        query.prepare(query_text)

        if parameters is not None:
            if isinstance(parameters, dict):
                for key, value in parameters.items():
                    query.bindValue(f":{key}", value)
            elif isinstance(parameters, tuple):
                # Single set of parameters (for delete or update queries)
                for value in parameters:
                    query.addBindValue(value)
            elif isinstance(parameters, list):
                # Batch operation (for insert queries)
                # for param_set in parameters:
                #     for i, value in enumerate(param_set):
                #         query.addBindValue(value)
                self.database.transaction()
                for param_set in parameters:
                    for value in param_set:
                        query.addBindValue(value)
                    if not query.exec():
                        self.database.rollback()
                        raise Exception(f"Error during batch execution: {query.lastError().text()}")
                self.database.commit()

        if not (isinstance(parameters, list) and parameters):
            if not query.exec():
                raise Exception(f"Error: Query execution failed with message - {query.lastError().text()}\n"+
                                f"QUERY: {query_text}\n" +
                                f"PARAMETERS: {parameters}")

    def fetch_data(self, query_text, parameters=None):
        """
        Executes a SELECT query and returns the fetched data.

        :param query_text: The SQL query string with placeholders.
        :param parameters: A dictionary where keys match the placeholders in the SQL query.
        :return: A list of dictionaries containing the query results.
        """
        query = QSqlQuery()
        query.prepare(query_text)

        for key, value in parameters.items():
            query.bindValue(f":{key}", value)

        if query.exec():
            result = []
            while query.next():
                row = {query.record().fieldName(i): query.value(i) for i in range(query.record().count())}
                result.append(row)

            return result
        else:
            raise Exception(f"Error: Query execution failed with message - {query.lastError().text()}\n"+
                            f"QUERY: {query_text}\n" +
                            f"PARAMETERS: {parameters}")
        
    def validate_data(self, data, required_fields):
        """
        Validate if all required fields are present in each data entry.

        :param data: List of data entries.
        :param required_fields: List of required field names.
        """
        for entry in data:
            if any(required_field not in entry for required_field in required_fields):
                missing = ', '.join(required_field for required_field in required_fields if required_field not in entry)
                raise ValueError(f"Missing required fields: {missing}")

    def insert_data(self, table_name, data):
        """
        Insert a list of data entries into the given table.

        :param table_name: Name of the database table.
        :param data: List of data entries.
        """
        if not data:
            return
        #TODO: support check data is list or not
        fields = data[0].keys()  # Assuming all data entries have the same structure
        placeholders = ', '.join(['?' for _ in fields])
        query = f"INSERT INTO {table_name} ({', '.join(fields)}) VALUES ({placeholders})"

        values = [tuple(entry[field] for field in fields) for entry in data]
        self.execute_sql_query(query, values)

    def insert(self, **kwargs):
        table = kwargs.get('table')
        data = kwargs.get('data')

        if table is None or data is None:
            raise ValueError('table and  data is required!')

        #TODO: self.validate_data(data, ['UserID', 'Password'])
        self.insert_data(table, data)

    def delete(self, **kwargs):
        table = kwargs.get('table')
        column = kwargs.get('column')
        values_list = kwargs.get('values_list')

        if table is None or column is None or values_list is None :
            raise ValueError('table, column and values_list are required!')
        
         # Preparing the parameters for the IN clause
        placeholders = ', '.join(['?' for _ in values_list])

        # Preparing the parameters for the IN clause
        in_params = tuple(values_list)

        # Constructing the DELETE query
        query = f"DELETE FROM {table} WHERE {column} IN ({placeholders})"

        self.execute_sql_query(query, in_params)

    def select(self, **kwargs):
        table = kwargs.get('table')
        columns = kwargs.get('columns', '*')
        conditions = kwargs.get('conditions')  # SQL conditions as a string
        parameters = kwargs.get('parameters', {})  # Parameters for the query

        if table is None:
            raise ValueError('Table name is required!')
        
        query = f"SELECT {columns} FROM {table}"
        if conditions:
            query += f" WHERE {conditions}"

        return self.fetch_data(query, parameters)
    
    def update(self, **kwargs):
        table = kwargs.get('table')
        data = kwargs.get('data' , {})
        expressions = kwargs.get('expressions', {})# Special SQL expressions
        conditions = kwargs.get('conditions')
        parameters = kwargs.get('parameters', {})

        if table is None:
            raise ValueError('Table name is required!')
        
        set_parts = []
        for key, value in data.items():
            set_parts.append(f"{key} = :{key}")
            parameters[key] = value

        for key, expr in expressions.items():
            set_parts.append(f"{key} = {expr}")

        set_clause = ', '.join(set_parts)
        query = f"UPDATE {table} SET {set_clause}"
        if conditions:
            query += f" WHERE {conditions}"

        self.execute_sql_query(query, parameters)

    #------------Funtion helper------------------------
    def add_seeding_action(self, uid, link, action):
        seedings_data = [{
            'UserID'    : uid,
            'Post_Link' : link,
            'Action'    : action,
            'TIME'      : datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }]
        self.insert(table='seedings', data=seedings_data)
        
    def add_post_history(self, active_id, group_link, post_link, status):
        history_data = [{
            'UserID'    : active_id,
            'Group_Link': group_link,
            'Post_Link' : post_link,
            'Status'    : status,
            'TIME'      : datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }]
        self.insert(table='posts', data=history_data)

    def get_account_test(self):
        group =  self.select(table='groups_tita', 
                    conditions = "Type = :type and Category='Công khai ' and Interact='Page' and (Status IS NULL or Status = 'Free')",
                    parameters = {'type': 'MAY'})
        
        return(len(group))
    
    def get_group_free(self, group_type):
        groups =  self.select(
                    table       ='groups_tita',
                    columns      = 'Group_Link',
                    conditions  = "Type = :type and Category='Công khai ' and Interact='Page' and (Status IS NULL or Status = 'Free')",
                    parameters  = {'type': group_type})
        return [entry.get('Group_Link') for entry in groups]
    
    def get_post_approved_link(self):
        groups =  self.select(
                    table       ='posts',
                    columns     = 'Post_Link',
                    conditions  = "Status = :status",
                    parameters  = {'status': 'Approved'})
        return [entry.get('Post_Link') for entry in groups]
    
    def get_seeding_liked_link(self, uid):
        groups =  self.select(
                    table       ='seedings',
                    columns     = 'Post_Link',
                    conditions  = "Action='Liked' and UserID=:userid",
                    parameters  = {'userid': uid})
        return [entry.get('Post_Link') for entry in groups]
    
    def get_account_pageid(self, uid):
        pageid =  self.select(
                    table       ='accounts',
                    columns     = 'PageID',
                    conditions  = "UserID=:userid",
                    parameters  = {'userid': uid})

        return pageid[0].get('PageID', None) if pageid else None

    def get_proxy_extension(self, id):
        if not id:
            return None
        proxy_extension =  self.select(
                    table       ='proxy',
                    columns     = 'zip_proxy',
                    conditions  = "ID=:id",
                    parameters  = {'id': id})
        return proxy_extension[0].get('zip_proxy', None) if proxy_extension else None
    
    def update_account_status(self, uid, status):
        self.update(
                table       = 'accounts', 
                data        = {'Status': status}, 
                conditions  = "UserID = :userid",
                parameters  = {'userid': uid}
                )
        
    def update_account_message(self, uid, message):
        self.update(
                table       = 'accounts', 
                data        = {'Message': message}, 
                conditions  = "UserID = :userid",
                parameters  = {'userid': uid}
                )
        
    def update_group_interact(self, link, interact):
        self.update(
                table       = 'groups_tita', 
                data        = {'Interact': interact}, 
                conditions  = "Group_Link = :link",
                parameters  = {'link': link}
                )
        
    def update_post_status(self, pending_post, status):
        self.update(
                table       = 'posts', 
                data        = {'Status': status}, 
                conditions  = "Post_Link = :pending_post",
                parameters  = {'pending_post': pending_post}
                )
        
    def update_post_commented_counts(self, link):
        self.update(
                table       = 'posts', 
                expressions   = {'Commented': 'Commented + 1'},
                conditions  = "Post_Link = :link",
                parameters  = {'link': link}
                )
    
    def update_post_liked_counts(self, link):
        self.update(
                table       = 'posts', 
                expressions   = {'Liked': 'Liked + 1'},
                conditions  = "Post_Link = :link",
                parameters  = {'link': link}
                )
        
    def update_group_posted_status(self, pageid, link, status):
        self.update(
                table       = 'groups_tita', 
                data        = {
                                'Status': status, 
                                'Post_Time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                'Posted_Page':pageid
                            },
                conditions  = "Group_Link = :link",
                parameters  = {'link': link}
                )
        

    #-----------------------------------------------------------------------------------------------------------

    def create_group_table(self, table_name):
        if table_name is None:
            raise ValueError('Table name is required!')
        
        query = f"""CREATE TABLE IF NOT EXISTS {table_name} (ID integer primary key, Group_Link TEXT UNIQUE, Group_Name TEXT, Category TEXT, Numbers INTEGER, Details TEXT,Type TEXT, Status TEXT, Post_Time TEXT)"""

        self.execute_sql_query(query)

    def get_account_info(self, uid):
        ret_account =  self.select(
                    table       ='accounts',
                    conditions  = "UserID = :userid",
                    parameters  = {'userid': uid})
        
        if len(ret_account) != 1:
            raise Exception("Can't find user ID")
        account = ret_account[0]
        proxy_extension = self.get_proxy_extension(account.get('ProxyID', None))
        return AccountInfo(
            account['UserID'],
            account['Password'],
            proxy_extension,
            account['Code2FA'],
            account['Cookie'],
            account['Email'],
            account['PassEmail'],
        )
        return UserAccount(**account[0])

        # uid, password, proxy, secret_2fa, cookie, email, pass_email  = self.sql_utils.get_accounts(uid)
        # proxy_extension = self.get_proxy_extension(proxy)
        # return AccountInfo(uid, password, proxy_extension, secret_2fa, cookie, email, pass_email)
    

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
    
    def add_group_scan(self, table, groups):
        self._delete_all(table)

        self.insert(table=table,
                    data= [asdict(group) for group in groups])

    def _delete_all(self, table):
        if table is None:
            raise ValueError('Table name is required!')

        query = f"DELETE FROM {table}"
        self.execute_sql_query(query)

    def close_database(self):
        self.database.close()