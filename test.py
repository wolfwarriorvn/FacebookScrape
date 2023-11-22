from PySide6.QtSql import QSqlQuery, QSqlDatabase

connection_name = 'name'
db = QSqlDatabase.addDatabase('QSQLITE', connection_name)

# Perform your database operations here

# Close the database connection
db.đa
db.close()
del db

# Remove the database connection
QSqlDatabase.removeDatabase(connection_name)