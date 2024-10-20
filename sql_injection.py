import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")

# Insecure Code Example
# This code is vulnerable to SQL Injection attacks because it directly uses user input in the query.

# Try to enter the following input when prompted: ' OR '1'='1
user_input = input("Enter your username: ")
query = f"SELECT * FROM users WHERE username = '{user_input}'"
print(f"Executing query: {query}")
cursor.execute(query)

result = cursor.fetchone()
if result:
    print("User found:", result)
else:
    print("User not found.")

# Secure Code Example (commented out)
# To prevent SQL Injection, always use parameterized queries.
# Uncomment the code below to use the secure version.
'''
user_input = input("Enter your username: ")
query = "SELECT * FROM users WHERE username = ?"
print(f"Executing query: {query} with parameter {user_input}")
cursor.execute(query, (user_input,))
result = cursor.fetchone()
if result:
    print("User found:", result)
else:
    print("User not found.")
'''
