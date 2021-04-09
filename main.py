import mysql.connector as sql
import csv, sys

data = []
with open('data.csv') as f:
	csv_reader = csv.reader(f, delimiter=",")
	for row in csv_reader:
		data.append(tuple(row[2:]))

conn = sql.connect(
	host='localhost',
	user='Nux', 
	password='password',
	database='db')

if conn.is_connected:
	print('SQL Connect')

db = conn.cursor()

db.execute("CREATE TABLE spearpart_hp (id INT AUTO_INCREMENT PRIMARY KEY, nama_barang VARCHAR(255), harga VARCHAR(255), stok VARCHAR(255), terjual VARCHAR(255), rating VARCHAR(255))")
db.execute("SHOW TABLES")

for i in db:
	print(i)

query = "INSERT INTO spearpart_hp (nama_barang, harga, stok, terjual, rating) VALUES (%s, %s, %s, %s, %s)"
db.executemany(query, data)

conn.commit()

print(db.rowcount, "was inserted.") 