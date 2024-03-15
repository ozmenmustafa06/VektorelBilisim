import pgzrun
from pgzero.actor import Actor

WIDTH = 600 # Pencere Genişliği
HEIGHT = 300 # Pencere Yüksekliği

TITLE = "Uzaylı Yarışı" # Oyunun Adı 
FPS = 30 # Saniyedeki kare sayısı

# Nesneler
uzayli = Actor('uzaylı', (50, 240))
arkaplan = Actor("uzaylı_arkaplan")
kutu = Actor('uzaylı_kutu', (550, 265))

def draw():
    arkaplan.draw()
    uzayli.draw()
    kutu.draw()
    
def update(dt):
    # Kutunun Hareketi
    if kutu.x > - 20:
        kutu.x = kutu.x - 5
        kutu.angle = kutu.angle + 5
    else:
        kutu.x = WIDTH + 20
    
    if keyboard.left and uzayli.x > 20: # sol
        uzayli.x = uzayli.x - 5
    elif keyboard.right and uzayli.x < 580:
        uzayli.x = uzayli.x + 5
        
    
    if keyboard.space: # Zıplama
        uzayli.y = 100
        animate(uzayli, tween='bounce_end', duration=2, y=240)

pgzrun.go() 



