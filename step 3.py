import sqlite3
import pandas as pd
import os
df = pd.read_csv(r"C:\Users\HP\Downloads\sentimentdataset.csv")
print(df.head())
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, "sentiment.db")

conn = sqlite3.connect(db_path)
df.to_sql('sentiment_table', conn, if_exists='replace', index=False)

cursor = conn.cursor()
cursor.execute("SELECT * FROM sentiment_table LIMIT 5")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
