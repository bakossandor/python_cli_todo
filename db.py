import sqlite3


def usedb(add=False, delete=False, data=None, delete_num=None):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE if not exists todo (num int, data text)''')
    if add == True:
        insert(c, data)
    if delete == True:
        delete_this(c, delete_num)
    conn.commit()
    c.execute('SELECT * FROM todo ORDER BY num')
    resp = c.fetchall()
    conn.close()
    return resp

def insert(cursor, data):
    cursor.execute(f"INSERT INTO todo VALUES ({data[0]}, '{data[1]}')")

def delete_this(cursor, delete_num):
    cursor.execute(f"DELETE FROM todo WHERE num = {delete_num}")