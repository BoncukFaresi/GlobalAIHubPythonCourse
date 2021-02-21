class word():
    def __init__(self,word):
        self.word=word.upper()
        self.w_rd=list(self.word)
        self.harf=set(self.word)
        self.sayi=len(self.harf)

class man():
    def __init__(self):
        self.can=10
    def yanlis(self):
        if self.can>0:
            self.can-=1
            print("Yanlış tahmin")
            print("Kalan can: ",self.can )


kelime=word("ogrenme")
adam=man()
found=set()
past=set()
i=1
while True:
    print("\t",end="")
    for x in kelime.w_rd:
        if x in found:
            print(x,end="")
        else:
            print("_",end="")
    print(" ")
    guess=input(str(i)+". Tahmin :").upper()
    if guess not in past:
        if guess in kelime.w_rd:
            found.add(guess)
        else:
            adam.yanlis()
            if adam.can==0:
                print("!!!!!!!!Oyunu kaybettin!!!!!!!!!")
                break
    else:
        print("Bu harfi daha önce girdiniz")
        continue
    past.add(guess)
    i+=1
    if kelime.sayi == len(found):
        print("!!!!!!!!!!!!TEBRİKLER KAZANDINIZ!!!!!!!!!!!!!")
        print("Kelimeniz: ",kelime.word.upper())
        break


    
