ad= "Haldun"

# for a in range(10):
#        ad="Mustafa"
#    print(ad)

def deneme():
    global ad
    ad="Mustafa"
    print(ad)

deneme(deneme)
print(ad)
deneme()