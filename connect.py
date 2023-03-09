import sqlite3 as sql # import thw SQLite3 module

# connect() is connection method
conn= sql.connect("SQLite/flimflix.db")

# cursor object
cursor =conn.cursor()




