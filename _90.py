import sqlite3

# creating file path
dbfile = 'database.db'
# Create a SQL connection to our SQLite database
con = sqlite3.connect(dbfile)

# creating cursor
cur = con.cursor()

# query
query = '''
SELECT * FROM countries
WHERE area > 2000000
'''

# reading all table names
countries = cur.execute(query)

# reading data
names = [d[0] for d in cur.description]

with open('countries_big_area.txt', 'a') as file:
    file.write(','.join(names))
    for row in countries:
        file.write('\n')
        for country in row:
            file.write(str(country) + ',')

# Be sure to close the connection
con.close()