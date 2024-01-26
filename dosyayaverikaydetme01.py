dosya = ("Rehber.txt","a")
ad=input("Kaydedilecek Ad-Soyad:")
numara=input("Kaydedilecek numara:")

veri=ad+" "+numara+"\n"
dosya.write(veri)
dosya.close()