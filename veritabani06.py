try:
    import mysql.connector
    xxx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="pythondersleri"
        )
    print("Veritabanına başarıyla bağlandı.")
    print(xxx)

    try:
        secilenvt=xxx.cursor() #veritabanı seçim işlemi USE .....

        a="INSERT INTO ogrenciler (Ad, Telefon) VALUES (%s,%s)"
        b=("Mustafa Özmen","05442554157")

        secilenvt.execute(a, b) 
        print("Veritabanındaki tabloya kişi başarıyla eklendi.")
    except mysql.connector.Error as hata:
        print(f"Veritabanındaki tabloya kişi eklenemedi. Hata:{hata}")

except mysql.connector.Error as xx:
    print("Veritabanına bağlanırken bir hata oluştu.")
    print(f"Hata kodu: {xx}")