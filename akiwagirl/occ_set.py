import sqlite3

occupancies = [0 for _ in range(18)]
occupancies[0] = 1
occupancies[16] = 1
occupancies[17] = 1


con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

for i, occupancy in enumerate(occupancies):
  cur.execute("UPDATE seat_occupancy set occupancy={} where id={};".format(occupancy,i+1))
con.commit()
con.close()
