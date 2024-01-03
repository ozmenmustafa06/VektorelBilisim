puan=int(input("Matematik puanın kaç?"))
cins=input("Cinsiyetin nedir?")
if puan<0 or puan>100:
    print("Yanlış giriş")
else:
    if puan>85:print("Süper")
    elif puan>70:print("İyi")
    elif puan>50:print("Geçtin")
    else:print("Kaldın")
if puan>85 and (cins=="erkek" or cins=="Erkek"):
    print("Futbol takımına girebilirsin")
else:print("Takıma giremezsin")
