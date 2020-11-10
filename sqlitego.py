'''
https://docs.python.org/2/library/sqlite3.html
'''
import sqlite3
conn = sqlite3.connect("test.db")
#df.to_sql("table_name", con, if_exists="replace", index=False)
#con.close()

c= conn.cursor()
c.execute(' CREATE TABLE users3( id text, pw text, level real)')
conn.commit()

c.execute('SELECT * FROM users3')
c.fetchall()

#conn.close()

'''
c.execute('insert into users3 values (?,?,?)', ['lon','pwpw',5] )
#print(c.fetchall())
[('lon', 'pwpw', 5.0)]

c.execute('select * from sqlite_master')
<sqlite3.Cursor object at 0x0393AA20>
>>> c.fetchall()

'''


