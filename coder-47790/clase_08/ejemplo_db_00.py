import sqlite3

# Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect('mi_primer_base_de_datos.db')

cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    identificacion INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL
)
''')

# Insert some sample data
users_data = [
    ('Alice', 28),
    ('Bob', 22),
    ('Charlie', 30),
    ('David', 25)
]
cursor.executemany('INSERT INTO users (nombre, edad) VALUES (?, ?)', users_data)
conn.commit()
