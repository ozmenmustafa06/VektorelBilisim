class calisan:
    def __init__(self,a,b,c):
        print("__init__ fonksiyonu çalışıyor.")
        self.name=a
        self.surname=b
        self.age=c
    def show_info(self):
        print(f"Ad:{self.name}  Soyad:{self.surname}   Yaş:{self.age}")

calisan1=calisan("Ali","Veli",20)
print(calisan1.name,calisan1.surname,calisan1.age)

calisan2=calisan("Ahmet","Mehmet",25)
print(calisan2.name,calisan2.surname,calisan2.age)

calisan1.show_info()

calisan.show_info(calisan2)