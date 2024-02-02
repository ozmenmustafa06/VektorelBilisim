class Ogrenci:
    AdSoyad = "---"
    NotOrtalamasi = ""
    DisiplinCezasi = 0

    # def __init__(self):
    #     self.AdSoyad = "Tanımsız"
    #     self.Numara = 0 
        
    def Bilgi(self):
        print ("Metod ile: Adı Soyadı:",self.AdSoyad,", Numarası:",self.Numara)


ogrenci1 = Ogrenci()
Ogrenci.AdSoyad="Mustafa"
ogrenci2=Ogrenci()
ogrenci3=Ogrenci()
print("Sınıftaki adSoyad değeri:",Ogrenci.AdSoyad)
print(ogrenci1.AdSoyad)
print(ogrenci2.AdSoyad)
print(ogrenci3.AdSoyad)


# ogrenci1.Bilgi()
