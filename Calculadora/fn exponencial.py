def exp(n):
    x=1
    i=0
    suma=0
    while abs(x)>=(10**-7):
        x=(n**i)/factorial(i)
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
n=float(input())
print(exp(n))
