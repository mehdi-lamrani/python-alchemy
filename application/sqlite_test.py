import sqlite3 as sql

con = sql.connect('user.db')
mycur = con.cursor()
mycur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
available_tables=(mycur.fetchall())
mycur.execute("SELECT name FROM users ")
users=(mycur.fetchall())
print(available_tables)
print(users)