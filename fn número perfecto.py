a=int(input())
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
b=perfecto(a)
print(b)

