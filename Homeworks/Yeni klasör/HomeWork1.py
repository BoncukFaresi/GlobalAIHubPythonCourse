# Home work 1
# Generating a 3x3 matrix with 9 random prime numbers.
# (you have to do it using the for loop)



i=0
liste=list()
for q in range(2,100):
    blnb=0
    for c in range(1,q):
        if q%c==0:
            blnb+=1
        else:
            continue
    if blnb<=1:
        liste.append(q)
        i+=1
    if i==9:
        break
print(liste)
i=0
while i<9:
    print(liste[i:i+3])
    i+=3
