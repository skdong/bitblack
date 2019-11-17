import sqlite3

db = sqlite3.connect("space/names.db")

c = db.cursor()

c.execute("""
create table name
(NAME INT PRIMARY KEY NOT NULL,
status )
""")

