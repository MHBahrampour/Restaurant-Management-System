import sqlite3

# Create connection
con = sqlite3.connect('database.db')
# Create cursor
c = con.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS branch (
        id INTEGER NOT NULL,
        name TEXT NOT NULL,
        addr_state TEXT NOT NULL,
        addr_city TEXT NOT NULL,
        addr_street TEXT NOT NULL,
        date TEXT NOT NULL,
        PRIMARY KEY (id))'''
)

c.execute('''CREATE TABLE IF NOT EXISTS employee (
        id INTEGER NOT NULL,
        branch_id INTEGER NOT NULL,
        post TEXT NOT NULL,
        fname TEXT NOT NULL,
        lname TEXT NOT NULL,
        gender TEXT NOT NULL,
        salary TEXT NOT NULL,
        addr_state TEXT NOT NULL,
        addr_city TEXT NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (branch_id) REFERENCES branch (id))'''
)

c.execute('''CREATE TABLE IF NOT EXISTS customer (
        id INTEGER NOT NULL,
        fname TEXT NOT NULL,
        lname TEXT NOT NULL,
        gender TEXT NOT NULL,
        PRIMARY KEY (id))'''
)

c.execute('''CREATE TABLE IF NOT EXISTS salon (
        id INTEGER NOT NULL,
        capacity INTEGER NOT NULL,
        type INTEGER NOT NULL,
        PRIMARY KEY (id))'''
)

c.execute('''CREATE TABLE IF NOT EXISTS food (
        id INTEGER NOT NULL,
        chef_id TEXT NOT NULL,
        name TEXT NOT NULL,
        type TEXT NOT NULL,
        cost REAL NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (chef_id) REFERENCES employee (id))'''
)

temp = [
        (900, 13835, 'Chelo Morgh', 'Food', '25000'),
        (901, 13835, 'Chelo Kabab', 'Food', '35000'),
        (902, 23835, 'Pizza', 'FastFood', '20000'),
        (903, 23877, 'Hot Dog', 'FasFood', '15000'),
        (904, 25835, 'Pizza', 'FastFood', '25000'),
        (905, 25877, 'Koofte', 'Food', '30000'),
        (906, 35198, 'Estamboli', 'Food', '20000'),
        (907, 35211, 'Dampokht', 'Food', '15000'),
        (908, 35298, 'Chelo Gheime', 'Food', '25000'),
        (909, 35511, 'Pizza', 'FastFood', '27000'),
        (910, 35511, 'Chelo Morgh', 'Food', '30000'),
]

c.executemany('INSERT INTO food VALUES (?,?,?,?,?)', temp)

# Save (commit) the changes
con.commit()

# Close the connection
con.close()
