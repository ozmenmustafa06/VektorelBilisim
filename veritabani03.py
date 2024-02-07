try:
    import mysql.connector
    xxx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"
        )
    print("Veritabanına başarıyla bağlandı.")
    print(xxx)

    try:
        secilenvt=xxx.cursor() #veritabanı seçim işlemi USE .....
        secilenvt.execute("CREATE DATABASE pythondersleri") # veritabanında SQL komutu çalıştırma işlemi
        print("Veritabanı oluşturuldu.")
    except mysql.connector.Error as hata:
        print(f"Veritabanı oluşturulamadı. Hata:{hata}")

except mysql.connector.Error as xx:
    print("Veritabanına bağlanırken bir hata oluştu.")
    print(f"Hata kodu: {xx}")