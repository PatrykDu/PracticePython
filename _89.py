import sqlite3

# creating file path
dbfile = 'database.db'
# Create a SQL connection to our SQLite database
con = sqlite3.connect(dbfile)

# creating cursor
cur = con.cursor()

# query
query = '''
SELECT country text FROM countries
WHERE area > 2000000
'''

# reading all table names
countries = cur.execute(query)

for country in countries:
    print(*country)

# Be sure to close the connection
con.close()
