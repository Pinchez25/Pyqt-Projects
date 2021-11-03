from PyQt6.QtSql import *

conn = QSqlDatabase.addDatabase('QPSQL')
conn.setHostName('localhost')
conn.setUserName('postgres')
conn.setPassword('1234')
conn.setDatabaseName('postgres')

conn.open()

# print(conn.databaseName())
# print(conn.connectionName())
print(conn.isOpen())

if not conn.open():
    print(conn.lastError().databaseText())
# print(conn.isDriverAvailable('QSQLITE'))

query = QSqlQuery()
query.exec("""
    CREATE TABLE accounts (
	user_id serial PRIMARY KEY,
	username VARCHAR ( 50 ) UNIQUE NOT NULL,
	password VARCHAR ( 50 ) NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
        last_login TIMESTAMP 
)

""")

print(conn.tables())

result = query.exec("""select password from "user" where id = 1""")
print(result)