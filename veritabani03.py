try:
    import mysql.connector
    xxx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"
        )
    print("Veri tabanına başarıyla bağlandı.")
    print(xxx)

    secilenvt=xxx.cursor() #veritabanı seçim işlemi USE .....
    secilenvt.execute("SHOW DATABASES")
    print("Veri Tabanları:")
    for x in secilenvt:
        print(x)

except mysql.connector.Error as xx:
    print("Veri tabanına bağlanırken bir hata oluştu.")
    print(f"Hata kodu: {xx}")