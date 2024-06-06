from PySide6.QtCore import QObject
from PySide6.QtSql import QSqlTableModel, QSqlQuery, QSqlDatabase

from setting import main_setting
from dataclasses import dataclass, asdict
from model.request import DeleteRequest, InsertRequest, SelectRequest, UpdateRequest
import time
import uuid

# Database Operations Class
class Op:
    INSERT = 'insert'
    SELECT = 'select'
    DELETE = 'delete'
    UPDATE = 'update'

class DatabaseRequest:
    def __init__(self, operation, table, data=None, conditions=None, parameters=None):
        self.operation = operation
        self.table = table
        self.data = data
        self.conditions = conditions
        self.parameters = parameters

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
    def __init__(self, connection_name=None):
        super().__init__()
        self.connection_name = connection_name
        if connection_name:
            self.database = QSqlDatabase.addDatabase('QSQLITE', self.connection_name)
        else:
            self.database = QSqlDatabase.addDatabase('QSQLITE')
        self.database.setDatabaseName(main_setting.database)

        if not self.database.open():
            raise Exception("Error: Unable to open the database connection.")
        
        self.query = QSqlQuery(self.database)  

    
    def execute_sql_query(self, query_text, parameters=None):
        """
        Executes an SQL query using the provided parameters.

        :param query_text: The SQL query string with placeholders.
        :param parameters: A dictionary where keys correspond to placeholders in the query.
        """
        # query = QSqlQuery(self.database)
        self.query.prepare(query_text)

        if parameters is not None:
            if isinstance(parameters, dict):
                for key, value in parameters.items():
                    self.query.bindValue(f":{key}", value)
            elif isinstance(parameters, tuple):
                # Single set of parameters (for delete or update queries)
                for value in parameters:
                    self.query.addBindValue(value)
            elif isinstance(parameters, list):
                # Batch operation (for insert queries)
                # for param_set in parameters:
                #     for i, value in enumerate(param_set):
                #         query.addBindValue(value)
                self.database.transaction()
                for param_set in parameters:
                    for value in param_set:
                        self.query.addBindValue(value)
                    if not self.query.exec():
                        self.database.rollback()
                        raise Exception(f"Error during batch execution: {self.query.lastError().text()}")
                self.database.commit()

        if not (isinstance(parameters, list) and parameters):
            if not self.query.exec():
                raise Exception(f"Error: Query execution failed with message - {self.query.lastError().text()}\n"+
                                f"QUERY: {query_text}\n" +
                                f"PARAMETERS: {parameters}")

    def fetch_data(self, query_text, parameters=None):
        """
        Executes a SELECT query and returns the fetched data.

        :param query_text: The SQL query string with placeholders.
        :param parameters: A dictionary where keys match the placeholders in the SQL query.
        :return: A list of dictionaries containing the query results.
        """
        # query = QSqlQuery(self.database)
        self.query.prepare(query_text)

        for key, value in parameters.items():
            self.query.bindValue(f":{key}", value)

        if self.query.exec():
            result = []
            while self.query.next():
                row = {self.query.record().fieldName(i): self.query.value(i) for i in range(self.query.record().count())}
                result.append(row)

            return result
        else:
            raise Exception(f"Error: Query execution failed with message - {self.query.lastError().text()}\n"+
                            f"QUERY: {query_text}\n" +
                            f"PARAMETERS: {parameters}")

    def insert(self, request: InsertRequest):
        """
        Insert a list of data entries into the given table.

        :param table_name: Name of the database table.
        :param data: List of data entries.
        """
        if not request.data:
            return
        #TODO: support check data is list or not
        fields = request.data[0].keys()
        placeholders = ', '.join(['?' for _ in fields])
        query = f"INSERT INTO {request.table} ({', '.join(fields)}) VALUES ({placeholders})"
        values = [tuple(entry[field] for field in fields) for entry in request.data]
        self.execute_sql_query(query, values)

    def delete(self, request: DeleteRequest):
        placeholders = ', '.join(['?' for _ in request.values_list])
        query = f"DELETE FROM {request.table} WHERE {request.column} IN ({placeholders})"
        self.execute_sql_query(query, tuple(request.values_list))

    def select(self, request: SelectRequest):
        query = f"SELECT {request.columns} FROM {request.table}"
        if request.conditions:
            query += f" WHERE {request.conditions}"
        return self.fetch_data(query, request.parameters)
    
    def update(self, request: UpdateRequest):
        set_parts = [f"{key} = :{key}" for key in request.data.keys()]
        if request.expressions:
            set_parts.extend([f"{key} = {expr}" for key, expr in request.expressions.items()])
        set_clause = ', '.join(set_parts)
        query = f"UPDATE {request.table} SET {set_clause}"
        if request.conditions:
            query += f" WHERE {request.conditions}"

        self.execute_sql_query(query, {**request.data, **(request.parameters or {})})

    def _delete_all(self, table):
        if table is None:
            raise ValueError('Table name is required!')

        query = f"DELETE FROM {table}"
        self.execute_sql_query(query)

    def close_database(self):
        self.query.finish()
        del self.query
        self.database.close()
        del self.database
        QSqlDatabase.removeDatabase(self.connection_name)
