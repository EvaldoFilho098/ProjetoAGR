import sqlite3

conn = sqlite3.connect('AGR.db')

cursor = conn.cursor()

# lendo os dados
cursor.execute("""
SELECT * FROM AGR;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()