#sayi1=int(input("Bir sayı giriniz:"))
#    sayi2=int(input("Bir sayı giriniz:"))
#    print("Toplamı:", sayi1+sayi2)

try:
    sayi1 = int(input("Bir sayı giriniz:"))
    sayi2 = int(input("Bir sayı giriniz:"))
    print("Toplamı:", sayi1 + sayi2)

except ValueError:
    print("Girilen değerlerde sorun var.")

except ZeroDivisionError:
    print("0'a bölüm hatası")

except:
    print("Bir hata oluştu.")

finally:
    print("Hata oluşma ihtimali olan blok bitti.")