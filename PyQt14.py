from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox

app = QApplication([])

class Login(QMainWindow):
    def tiklama1(self):
        kullanici = self.ka.text()
        sifre = self.sf.text()
        dogruKa = "q"
        dogruSf = "q"
        mesaj = QMessageBox()

        if kullanici == dogruKa and sifre == dogruSf:
            self.close() # Login penceresini kapat
            self.xx = AnaEkran()
            self.xx.show()
        else:
            mesaj.setText("Yetki yok.")
            mesaj.exec()

    def __init__(self):
        super().__init__()

        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Kullanıcı adı:"))
        self.ka = QLineEdit()
        icerik.addWidget(self.ka)
        icerik.addWidget(QLabel("Şifre:"))
        self.sf = QLineEdit()
        self.sf.setEchoMode(QLineEdit.EchoMode.Password)

        icerik.addWidget(self.sf)
        bt = QPushButton("Giriş yap")
        icerik.addWidget(bt)

        bt.clicked.connect(self.tiklama1)

        pencere = QWidget()
        pencere.setLayout(icerik)
        self.setCentralWidget(pencere)

class AnaEkran(QMainWindow):
    def tiklama1(self):
        mesaj = QMessageBox()
        mesaj.setText("Uygulama1")
        mesaj.exec()

    def tiklama2(self):
        mesaj = QMessageBox()
        mesaj.setText("Uygulama2")
        mesaj.exec()

    def __init__(self):
        super().__init__()

        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("MASAÜSTÜ UYGULAMAMIZA HOŞ GELDİNİZ"))
        bt1 = QPushButton("Uygulama-1")
        icerik.addWidget(bt1)
        bt2 = QPushButton("Uygulama-2")
        icerik.addWidget(bt2)

        bt1.clicked.connect(self.tiklama1)
        bt2.clicked.connect(self.tiklama2)

        pencere = QWidget()
        pencere.setLayout(icerik)
        self.setCentralWidget(pencere)

ekran = Login()
ekran.show()
app.exec()
