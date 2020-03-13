def ln(n):
    x=1
    n=(n-1)/(n+1)
    i=0
    suma=0
    while abs(x)>=(10**-7):
        x=(n**(2*i+1))/(2*i+1)
        suma+=x
        i+=1
    return suma*2
n=float(input())
print(ln(n))
