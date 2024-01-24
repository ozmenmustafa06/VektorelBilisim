#sayi1=int(input("Bir sayı giriniz:"))
#    sayi2=int(input("Bir sayı giriniz:"))
#    print("Toplamı:", sayi1+sayi2)
hata = "var"
while hata == "var":
    try:
        sayi1 = int(input("Bir sayı giriniz:"))
        sayi2 = int(input("Bir sayı giriniz:"))
        print("Toplamı:", sayi1 + sayi2)
        hata = "yok"
    except:
        print("Hatalı giriş! Lütfen sayıları doğru formatta girin.")
        hata = "var"