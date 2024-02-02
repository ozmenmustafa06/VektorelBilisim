class Ilan():
    def __init__(self, n,b,s,a):
        self IlanNo=n
        self IlanBaslik=b
        self IlanSahibi=s
        self IlanAciklama=a

    def bilgi(self):
        print("No:",self.IlanNo,"Başlık:",self.IlanBaslik)

    def bilgi1(self):
        return "No:"+self.IlanNo+"Başlık:"+self.IlanBaslik

    def kaydet(self):
        d=open