try:
    import mysql.connector
    xxx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"
        database="pythondersleri"
        )
    print("Veritabanına başarıyla bağlandı.")
    print(xxx)

    try:
        secilenvt=xxx.cursor() #veritabanı seçim işlemi USE .....
        secilenvt.execute("CREATE TABLE ogrenciler (ad VARCHAR(255), telefon VARCHAR(255))") # veritabanında SQL komutu çalıştırma işlemi
        print("Veritabanında tablo başarıyla oluşturuldu.")
    except mysql.connector.Error as hata:
        print(f"Tablo oluşturulamadı. Hata:{hata}")

except mysql.connector.Error as xx:
    print("Veritabanına bağlanırken bir hata oluştu.")
    print(f"Hata kodu: {xx}")