import sqlite3

num=11

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

cur.execute("UPDATE num_current set num={};".format(num))
con.commit()
con.close()
