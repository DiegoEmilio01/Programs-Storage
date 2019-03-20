a=int(input())
z=int(input())
def perfecto (a):
    c=1
    div=0
    while c<a:
        if a%c==0:
            div=div+c
        c+=1
    if div==a:
        per=True
    else:
        per=False
    return (per)
n=0
print("Los numeros perfectos son:")
while a<=z:
    p=perfecto(a)
    if p:
        print(a)
    a+=1
