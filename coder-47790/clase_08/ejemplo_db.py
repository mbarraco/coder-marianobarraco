import sqlite3

# Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Create a table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
"""
)

# Insert some sample data
users_data = [("Alice", 28), ("Bob", 22), ("Charlie", 30), ("David", 25)]

cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users_data)

# Commit the changes (save them to the database)
conn.commit()

# Query the database: fetch all users
cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall()
print("All users:")
for user in all_users:
    print(user)

# Query the database: fetch users older than 25
cursor.execute("SELECT * FROM users WHERE age > 25")
older_users = cursor.fetchall()
print("\nUsers older than 25:")
for user in older_users:
    print(user)

# Close the database connection
conn.close()
