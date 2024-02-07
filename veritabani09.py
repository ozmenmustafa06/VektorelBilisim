import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="pythondersleri"
)

mycursor = mydb.cursor()

ad=input("Kaydedilecek isim: ")
no=input("Kaydedilecek numara: ")
a= "INSERT INTO ogrenciler (ad, telefon) VALUES (%s, %s)"
b= (ad, no)
mycursor.execute(a, b) 

mydb.commit()

print(mycursor.rowcount, "kayıt eklendi.")
