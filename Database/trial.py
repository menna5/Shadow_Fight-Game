# modules 
import sqlite3

# connecting database
con = sqlite3.connect('game.db')
cur = con.cursor()

# creating a table 
# cur.execute('CREATE TABLE "user" (name TEXT NOT NULL, id INTEGER, score INTEGER DEFAULT 0,date text default CURRENT_DATE, time text default CURRENT_TIME, PRIMARY KEY(id AUTOINCREMENT))')\

cur.execute('insert into user (name) values (\'Mena\')')
# cur.execute('update users set score= ? where id= ?', (new_score, id,))
rows = cur.execute('select * from user')
for row in rows:
    print(row)
# commiting changes and closing the database 
con.commit()
con.close()
