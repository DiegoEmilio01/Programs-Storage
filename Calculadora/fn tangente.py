def sen(n):
    n=n*3.1415926535897932/180
    x=1
    i=0
    suma=0
    while abs(x)>=(10**-8):
        x=((-1)**i)*(n**(2*i+1))/factorial(2*i+1)
        suma+=x
        i+=1
    return suma
def cos(n):
    n=n*3.1415926535897932/180
    x=1
    i=0
    suma=0
    while abs(x)>=(10**-8):
        x=((-1)**i)*(n**(2*i))/factorial(2*i)
        suma+=x
        i+=1
    return suma
def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)
def tg(n):
    return sen(n)/cos(n)
n=float(input())
print(tg(n))
