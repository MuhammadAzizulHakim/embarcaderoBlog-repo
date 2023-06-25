import sqlite3
 
con = sqlite3.connect('example.db')
 
cur = con.cursor()
 
# Create table
cur.execute('''CREATE TABLE stocks
            (date text, trans text, symbol text, qty real, price real)''')
 
# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
 
# Save (commit) the changes
con.commit()
 
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
 
# The data you’ve saved is persistent and is available in subsequent sessions:
con = sqlite3.connect('example.db')
cur = con.cursor()
 
# Do this instead
t = ('RHAT',)
cur.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(cur.fetchone())
 
# Larger example that inserts many records at a time
purchases = [('2021-03-28', 'BUY', 'IBM', 1000, 45.00),
    	     ('2021-04-05', 'BUY', 'MSFT', 1000, 72.00),
    	     ('2021-04-06', 'SELL', 'IBM', 500, 53.00),
             ]
cur.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
 
# Retrieve the data using iterator:
for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)