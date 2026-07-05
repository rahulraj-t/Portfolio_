import sqlite3

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

cursor.execute("SELECT * FROM Base_contact limit 20")

rows = cursor.fetchall()

print("ID | Name | Email | Content | Number")
print("-" * 80)

for row in rows:
    print(row)

conn.close()