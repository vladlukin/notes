import sqlite3


# conn = sqlite3.connect('notes.db')
#
# c = conn.cursor()
#
# # Create table
# c.execute('''CREATE TABLE stocks
#              (date text, trans text, symbol text, qty real, price real)''')
#
# # Insert a row of data
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#
# # Save (commit) the changes
# conn.commit()
#
# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# conn.close()

def add_note(id, body):
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    params = (id, body)
    c.execute("insert or replace into notes (id, body) values (?, ?) ", params)
    conn.commit()
    conn.close()
