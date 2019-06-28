import sqlite3

conn = sqlite3.connect("people.db")
c = conn.cursor()

#c.execute("CREATE TABLE people (first_name TEXT, last_name TEXT, age INTEGER);")

insert_query = '''INSERT INTO people(first_name, last_name, age)
                    VALUES('Jane', 'Smith', 44)'''
#c.execute(insert_query)

f_name = 'Joan'
i_query = 'INSERT INTO people(first_name) VALUES(?)'
c.execute(i_query, (f_name,))

conn.commit()
conn.close()