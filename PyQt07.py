from PyQt6.QtWidgets import *

app=QApplication([])
button=QPushButton('Tıkla')

def aaa():
    alert=QMessageBox()
    alert.setText('Tıkladın!')
    alert.exec()
    print("Tıklama gerçekleşti!!!")

button.clicked.connect(aaa)

button.show()
app.exec()