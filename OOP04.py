class calisan:
    def __init__(self,name,surname,age):
        print("__init__ fonksiyonu çalışıyor.")
        self.name=name
        self.surname=surname
        self.age=age

calisan1=calisan("Ali","Veli",20)
print(calisan1.name,calisan1.surname,calisan1.age)