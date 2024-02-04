class calisan:
    def __init__(self,a,b,c):
        print("__init__ fonksiyonu çalışıyor.")
        self.name=a
        self.surname=b
        self.age=c

calisan1=calisan("Ali","Veli",20)
print(calisan1.name,calisan1.surname,calisan1.age)