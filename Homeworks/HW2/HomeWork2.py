grades=list()
names=list()
stu=list()
for i in range(1,6):
    ad=input("Please enter "+str(i)+". students first name: ")
    sad=input("Please enter "+str(i)+". students last name: ")
    mid=int(input("Please enter students midterm grade: "))
    hw=int(input("Please enter students homework grade: "))
    fin=int(input("Please enter students final grade: "))
    nam=[ad.capitalize(),sad.capitalize()]
    gra=[mid,hw,fin]
    names.append(nam)
    grades.append(gra)
print(grades)
print(names)
info={(names[i][0]+" "+names[i][1]):grades[i] for i in range(5)}
print(info)
for i in info:
    top=0
    for q in info[i]:
        top+=q
    info[i]=top//3
print(info)
q=0
while q<5:
    maks=[0,0]
    for i in info:
        if info[i]>maks[1]:
            maks=[i,info[i]]
    stu.append(maks)
    del info[maks[0]]
    q+=1
q=0
while q<5:
    if q==0:
        print(q+1,".",stu[q][1],":",stu[q][0],"Tebrikler en yüksek notu siz aldınız!!!!!",sep=" ")
    else:
        print(q+1,".",stu[q][1],":",stu[q][0],sep=" ")
    q+=1
