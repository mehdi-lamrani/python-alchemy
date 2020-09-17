import sqlite3 as sql

con = sql.connect('user.db')
mycur = con.cursor()
mycur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
available_tables=(mycur.fetchall())
mycur.execute("SELECT name FROM users ")
users=(mycur.fetchall())
print(available_tables)
print(users)

###################################################################################################################################################
# CREATE A SQLite DB in PYCHARM
# https://phoenixnap.com/kb/how-to-create-mariadb-user-grant-privileges#:~:text=To%20create%20a%20new%20MariaDB,to%20a%20local%20MySQL%20server.
###################################################################################################################################################