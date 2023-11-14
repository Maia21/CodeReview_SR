import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, name TEXT)')
cursor.execute('INSERT INTO users (username, password, name) VALUES ("admin", "123", "Administrator")')

connection.commit()
connection.close()  