import pgzrun
from pgzero.actor import Actor

WIDTH = 600
HEIGHT = 300
TITLE = "UZAYLI"

karakter = Actor('uzayli', (50, 240))
kutu = Actor('kutu', (650, 260))
ari = Actor('arı', (750, 100))
arkaplan = Actor('uzaylı_arkaplan')

def draw():
    arkaplan.draw()
    karakter.draw()
    kutu.draw()
    ari.draw()

def update():
    kutu.x -= 4
    if kutu.x < 0:
        kutu.x = 650
    kutu.angle += 3

    ari.x -= 3
    if ari.x < 0:
        ari.x = 750

    if keyboard.left:
        karakter.x -= 5
    if keyboard.right:
        karakter.x += 5

pgzrun.go()
