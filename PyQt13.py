from PyQt6.QtWidgets import *
app = QApplication([])

class Login(QMainWindow):
    def tiklama1(self):
        # print("Tıklandı")
        kullanici=self.ka.text()
        sifre=self.sf.text()

        mesaj=QMessageBox()
        # mesaj.setText("Tıklandı")
        mesaj.setText(f"Kullanıcı adı: {kullanici} Şifre: {sifre}")
        mesaj.exec()


    def __init__(self):
        super().__init__()

        icerik=QVBoxLayout()
        icerik.addWidget(QLabel("Kullanıcı Adı:"))
        self.ka=QLineEdit()
        icerik.addWidget(self.ka)
        icerik.addWidget(QLabel("Şifre:"))
        self.sf=QLineEdit()
        icerik.addWidget(self.sf)
        bt=QPushButton("Giriş Yap")
        icerik.addWidget(bt)

        bt.clicked.connect(self.tiklama1)

        pencere=QWidget()
        pencere.setLayout(icerik)
        self.setCentralWidget(pencere)

ekran = Login()
ekran.show()
app.exec()