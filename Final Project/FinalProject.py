class yemek():
    def __init__(self):
        self.mix=False
        self.cooked=False
        self.oil=False
        self.salt=False
        self.taste=0
        self.sorunlar=["Çiğ","Tuzsuz","Yağsız"]#fonkisyonlara ekle
    def mixer(self):
        if not self.mix:
            self.mix=True
            self.taste+=10
    def cook(self):
        if "Çiğ" in self.sorunlar:
            self.sorunlar.remove("Çiğ")
        if self.cooked:
            self.cooked=False
            self.taste-=20
            self.sorunlar.append("Yanmış")
        else:
            self.cooked=True
            self.taste+=10
    def add_salt(self):
        if "Tuzsuz" in self.sorunlar:
            self.sorunlar.remove("Tuzsuz")
        if self.salt:
            self.salt=False
            self.taste-=20
            self.sorunlar.append("Çok Tuzlu")
        else:
            self.salt=True
            self.taste+=5
    def add_oil(self):
        if "Yağsız" in self.sorunlar:
            self.sorunlar.remove("Yağsız")
        if self.oil:
            self.oil=False
            self.taste-=10
            self.sorunlar.append("Çok Yağlı")
        else:
            self.oil=True
            self.taste+=5
    def ye(self):
        if 0 < self.taste < 30:
            print("Beceremedin......Puanın: ",self.taste)
        elif self.taste < 0:
            print("Berbat......Puanını duymak istemezsin")
        elif self.taste < 60:
            print("Ehh işte......Puanın: ",self.taste)
        elif self.taste < 90:
            print("İyi iş becerdin......Puanın: ",self.taste)
        else:
            print("Harika yemek yapıyorsun......Puanın: ",self.taste)
class menemen(yemek):
    def __init__(self):
        super().__init__()
        self.sucuk=False
        self.yumurta=False
        self.kasar=False
        self.biber=False
        self.domates=False
        self.sorunlar.extend(["Yumurtasız","Bibersiz","Domatessiz"])

    def add_sucuk(self):
        if self.sucuk:
            self.sucuk=False
            self.sorunlar.append("Çok sucuklu")
            self.taste-=20
        else:
            self.sucuk=True
            self.taste+=10
    def add_yumurta(self):
        if "Yumurtasız" in self.sorunlar:
            self.sorunlar.remove("Yumurtasız")
        if self.yumurta:
            self.yumurta:False
            self.sorunlar.append("Yumurta Kokuyor")
            self.taste-=40
        else:
            self.yumurta=True
            self.taste+=30
    def add_kasar(self):
        if self.kasar:
            self.kasar:False
            self.sorunlar.append("Çok peynirli")
            self.taste-=20
        else:
            self.kasar=True
            self.taste+=10
    def add_biber(self):
        if "Bibersiz" in self.sorunlar:
            self.sorunlar.remove("Bibersiz")
        if self.biber:
            self.biber:False
            self.sorunlar.append("Çok acı")
            self.taste-=30
        else:
            self.biber=True
            self.taste+=15
    def add_domates(self):
        if "Domatessiz" in self.sorunlar:
            self.sorunlar.remove("Domatessiz")
        if self.domates:
            self.domates:False
            self.sorunlar.append("Çok sulu")
            self.taste-=30
        else:
            self.domates=True
            self.taste+=15
    def doit(self):
        print("Menemen yapmaya başlayalım: ")
        while True:
            print("Öncelikle : 1) Yağ , sucuk ve biber kavurulur    2) Yağ ve biber kavrulur")
            self.add_oil()
            self.add_biber()
            self.cook()
            x=int(input("Seçimini yap:"))
            if x==1:
                self.add_sucuk()
                break
            elif x==2:
                break
            else:
                print("Lütfen geçerli bir cevap giriniz")
        while True:
            print("Sonra:   1)Domates koyulur ve pişirmeye devam edilir  2)Domates ve yumurta koyulur pişirmeye devam edilir ")
            self.add_domates()
            x=int(input("Seçimini yap:"))
            if x==2:
                self.add_yumurta()
                break
            elif x==1:
                break
            else:
                print("Lütfen geçerli bir cevap giriniz")
        while True:
            print("Ardından:   1)Yumurta koyulur ve karıştırılır  2)Yumurta ve tuz koyulup karıştırılır ")
            self.add_yumurta()
            x=int(input("Seçimini yap:"))
            if x==2:
                self.add_salt()
                break
            elif x==1:
                break
            else:
                print("Lütfen geçerli bir cevap giriniz")
        while True:
            print("Son olarak: 1)Kaşar peyniri eklenir ve biraz daha pişirilir   2)Kaşar peyniri eklenir ve menemenin altı kapatılır")
            self.add_kasar()
            x=int(input("Seçimini yap:"))
            if x==1:
                self.add_kasar()
                break
            elif x==2:
                break
            else:
                print("Lütfen geçerli bir cevap giriniz")
class kuru_fasulye(yemek):
    def __init__(self):
        super().__init__()
        self.sogan=False
        self.fasulye=False
        self.et=False
        self.salca=False
        self.sorunlar.extend(["Fasulyesiz olmaz","Soğan yok","Salça Yok"])
    def add_sogan(self):
        if "Soğan yok" in self.sorunlar:
            self.sorunlar.remove("Soğan yok")
        if self.sogan:
            self.sogan=False
            self.taste-=20
            self.sorunlar.append("Çok soğanlı")
        else:
            self.sogan=True
            self.taste+=10
    def add_fasulye(self):
        if "Fasulyesiz olmaz" in self.sorunlar:
            self.sorunlar.remove("Fasulyesiz olmaz")
        if self.fasulye:
            self.fasulye=False
            self.taste-=80
            self.sorunlar.append("Heryer Fasulye")
        else:
            self.fasulye=True
            self.taste+=40
    def add_et(self):
        if self.et:
            self.et=False
            self.taste-=20
            self.sorunlar.append("Çok Fazla Et")
        else:
            self.et=True
            self.taste+=10
    def add_salca(self):
        if "Salça Yok" in self.sorunlar:
            self.sorunlar.remove("Salça Yok")
        if self.salca:
            self.salca=False
            self.taste-=20
            self.sorunlar.append("Çok soğanlı")
        else:
            self.salca=True
            self.taste+=10
    def doit(self):
        print("Kuru Fasulye yapmaya başlayalım: ")
        while True:
            print("Öncelikle : 1)Soğan yağda kavrulur     2)Soğan salçayla yağda kavrulur ")
            self.add_oil()
            self.cook()
            self.add_sogan()
            x=int(input("Seçimini yap:"))
            if x==2:
                self.add_salca()
                break
            elif x==1:
                break
            else:
                print("Lütfen geçerli bir cevap giriniz")
        while True:
            print("Sonra:   1)Et katılır ve iyice karıştırılır  2)Fasulye Eklenir ve karıştırılır ")
            x=int(input("Seçimini yap:"))
            if x==1:
                self.add_et()
                break
            elif x==2:
                self.add_fasulye()
                break
            else:
                print("Lütfen geçerli bir cevap giriniz")
        while True:
            print("Ardından:   1)Et eklenip kavurulduktan sonra su ve tuz eklenir  2)Su ve tuz eklenip karıştırılır ")
            self.mixer()
            self.add_salt()
            x=int(input("Seçimini yap:"))
            if x==1:
                self.add_et()
                break
            elif x==2:
                break
            else:
                print("Lütfen geçerli bir cevap giriniz")
class soslu_makarna(yemek):
    def __init__(self):
        super().__init__()
        self.makarna=False
        self.salca=False
        self.kekik=False
        self.pulbiber=False
        self.sorunlar.extend(["Sadece sos mu yicez","Salçasız sos olmaz","Kekiksiz olmaz"])
    def add_makarna(self):
        if "Sadece sos mu yicez" in self.sorunlar:
            self.sorunlar.remove("Sadece sos mu yicez")
        if self.makarna:
            self.makarna=False
            self.sorunlar.append("Kim yiyecek bu kadar makarnayı")
            self.taste-=100
        else:
            self.makarna=True
            self.taste+=40
    def add_salca(self):
        if "Salçasız sos olmaz" in self.sorunlar:
            self.sorunlar.remove("Salçasız sos olmaz")
        if self.salca:
            self.salca=False
            self.sorunlar.append("Salça biraz ekşitmiş sanki")
            self.taste-=20
        else:
            self.salca=True
            self.taste+=10
    def add_kekik(self):
        if "Kekiksiz olmaz" in self.sorunlar:
            self.sorunlar.remove("Kekiksiz olmaz")
        if self.kekik:
            self.kekik=False
            self.sorunlar.append("Heryer Kekik")
            self.taste-=20
        else:
            self.kekik=True
            self.taste+=10
    def add_pulbiber(self):
        if self.pulbiber:
            self.pulbiber=False
            self.sorunlar.append("Çok Acı")
            self.taste-=50
        else:
            self.pulbiber=True
            self.taste+=10
    def doit(self):
        print("Soslu Makarna yapmaya başlayalım: ")
        while True:
            print("Öncelikle : 1) Makarna suda kaynatılır    2) Su Kaynatılır")
            x=int(input("Seçimini yap:"))
            self.cook()
            if x==1:
                self.add_makarna()
                break
            elif x==2:
                break
            else:
                print("Lütfen geçerli bir cevap giriniz")
        while True:
            print("Sonra:   1)Başka bir tavada salça yağ ile kavurulur  2)Salça yağsız kavrulur ")
            self.add_salca()
            x=int(input("Seçimini yap:"))
            if x==1:
                self.add_oil()
                break
            elif x==2:
                self.cook()
                break
            else:
                print("Lütfen geçerli bir cevap giriniz")
        while True:
            print("Ardından:   1)Sosa kekik, tuz ve pulbiber eklenir  2)Sosa kekik ve tuz eklenir ")
            self.add_kekik()
            self.add_salt()
            self.cook()
            x=int(input("Seçimini yap:"))
            if x==1:
                self.add_pulbiber()
                break
            elif x==2:
                break
            else:
                print("Lütfen geçerli bir cevap giriniz")
        while True:
            print("Son olarak: 1)Sos tencereye eklenir   2)Sos Tencereye eklenip karıştırılır")
            x=int(input("Seçimini yap:"))
            if x==2:
                self.mixer()
                break
            elif x==1:
                break
            else:
                print("Lütfen geçerli bir cevap giriniz")





food1=menemen()
food2=soslu_makarna()
food3=kuru_fasulye()
food1.doit()
food1.ye()
print(food1.sorunlar)
food2.doit()
food2.ye()
print(food2.sorunlar)
food3.doit()
food3.ye()
print(food3.sorunlar)
