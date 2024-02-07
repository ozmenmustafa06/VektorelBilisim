import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="pythondersleri"
)

mycursor = mydb.cursor()

# Adı "Mustafa" olan öğrencileri seçmek için parametrize edilmiş sorgu
sql = "SELECT * FROM ogrenciler WHERE ad = %s"
# Sorguyu parametrelerle birlikte çalıştırma
mycursor.execute(sql, ("Mustafa",))

xxx = mycursor.fetchall()

for x in xxx:
    for a in x:
        print(a, end=" ")
    print()
