import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="pythondersleri"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT ad FROM ogrenciler")
xxx=mycursor.fetchall()

for x in xxx:
    for a in x:
        print(a,end=" ")
    print()