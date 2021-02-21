import math
primes=list()
##############################################
def prime_first(x):
    check=False
    if x==2 or x==3 or x==5:
        return True
    else:
        for i in range(2,x):
            if x%i==0:
                check=True
    if check==False:
        return True
############################################
def prime_second(x):
    check=True
    y = int(math.sqrt(x))
    for i in primes:
        if i<=y:
            if x%i==0:
                check=False
    return check
#############################################
for i in range(2,1001):
        if i<501:
            if prime_first(i)==True:
                primes.append(i)
        else:
            if prime_second(i)==True:
                primes.append(i)
print(primes)
