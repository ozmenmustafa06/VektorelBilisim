import os
import time

os.mkdir("Veriler")
dosya=open("rehber.txt", "w")
dosya.write("Deneme1")
dosya.close()
time.sleep(6)
os.remove("Veriler")