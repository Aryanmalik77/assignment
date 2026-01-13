import requests
import sqlite3
import os
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()
print(data)
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, "my_data.db")
print(f"Saving to database at: {db_path}")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER,
        title TEXT,
        body TEXT
    )
''')
for item in data:
    cursor.execute('''
    INSERT INTO items ( id, title, body) VALUES (?, ?, ?)
    ''' ,( item['id'], item['title'], item['body']))
conn.commit()
cursor.execute("SELECT * FROM items")
rows = cursor.fetchall()
for row in rows:
     print(f"ID: {row[1]}")
     print(f"Title: {row[2]}")
     print(f"Body: {row[3]}")
conn.close()