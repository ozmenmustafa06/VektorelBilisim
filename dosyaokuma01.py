dosya = open("rehber.txt","r")

for a in range(5):
    okunan=dosya.read(5)
    print(okunan)