def columnas(lista,n):
    r="E"
    x=""
    y=" "
    z="  "
    for i in lista:
        if i[2]==n:
            if i[1]==0:
                x=i[0]
            elif i[1]==1:
                y=i[0]
            elif i[1]==2:
                z=i[0]
    print(x,y,z)
    if x==y and y==z:
        r=x
    return r

def filas(lista,n):
    r="E"
    l=""
    o=" "
    p="  "
    for i in lista:
        if i[1]==n:
            if i[2]==0:
                l=i[0]
            elif i[2]==1:
                o=i[0]
            elif i[2]==2:
                p=i[0]
    if l==o and o==p:
        r=l
    return r

lista=input().split(";")
terminar=False
for i in lista:
    print(i)
    if i[0]=="":
        print("No ha terminado")
        terminar=True
if terminar==False:
    for i in range(0,3):
        g=columnas(lista,i)
        if g!="E":
            print("Ganador:",g)
            terminar=True
if terminar==False:
    for i in range(0,3):
        g=filas(lista,i)
        if g!="E":
            print("Ganador:",g)
            terminar=True
if terminar==False:
    a=""
    b=" "
    c="  "
    for i in lista:
        if i[1]==i[2] and i[1]==0:
            a=i[0]
        if i[1]==i[2] and i[1]==1:
            b=i[0]
        if i[1]==i[2] and i[1]==2:
            c=i[0]
    if a==b and b==c:
        print("Ganador:",a)
        terminar=True
if terminar==False:
    a=""
    b=" "
    c="  "
    for i in lista:
        if i[1]==1 and i[2]==1:
            a=i[0]
        if i[1]==2 and i[2]==0:
            b=i[0]
        if i[1]==0 and i[2]==2:
            c=i[0]
    if a==b and b==c:
        print("Ganador:",a)
        terminar=True
if terminar==False:
    print("Empate")
