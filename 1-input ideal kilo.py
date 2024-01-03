print("İdeal Kilo Hesaplayıcı")
ad=input("Adınız nedir?")
boy=int(input(f"{ad} boyun kaç?"))
ikk=45.5+(2.3/2.54)*boy-152.4
ike=50+(2.3/2.54)*boy-152.4
print(f"{boy}cm boy için ideal erkek kilosu",ike,"dur.")
print(f"{boy}cm boy için ideal kadın kilosu",ikk,"dur.")
