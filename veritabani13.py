import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="okulvt"
)

mycursor = mydb.cursor()
sql = "UPDATE ogrenciler SET numarasi = '4441444' WHERE adiSoyadi= 'Ensar BUDAK'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "kayıt değiştirildi.")