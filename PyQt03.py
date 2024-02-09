import sys
from PyQt5.QtWidgets import *
app = QApplication(sys.argv)
window = QPushButton("Tıkla")
window.show()
label = QLabel('Merhaba!')
label.show()
app.exec()