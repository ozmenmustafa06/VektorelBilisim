import os

os.remove("silinecekdosya.txt")
if os.path.exists("silinecekdosya.txt"):
  os.remove("silinecekdosya.txt")
else:
  print("Silmek istediğiniz dosya yok")