def moverse(x,dx,Bat):
    if dx>=0:
        paso=1
    else:
        paso=-1
    z=0
    while z<abs(dx):
        if Bat>=5:
            x+=paso
            Bat=Bat-5
        else:
            print("Sin Bateria")
            z=abs(dx)
        z=z+1
    return(x,Bat)
def meterpos(f,ncolumna,d):
    i=0
    fila=""
    for a in f:
        if i==(ncolumna*3)+2:
            fila+=d
        else:
            fila+=a
        i+=1
    return fila
def mapear(mapa,filas):
    for i in range(0,filas):
        f=input()
        f=f.replace("[","|,")
        f=f.replace("]",",|")
        f=f.replace(",","")
        mapa.append(f)
    techo=" "+"_"*(len(f)-2)+" "
    piso=" "+"-"*(len(f)-2)+" "
    mapa.insert(0,techo)
    mapa.append(piso)
    return mapa    
def limpiar(a):
    p=a.find("O")+3
    n=a[p]
    op="OP "+n
    a=a.replace(op,"")
    return(op,a)

pos=input().replace("(","").replace(")","")
pos=pos.split(",")
x=int(pos[0])
y=int(pos[1])
d=input()
filas=int(input())
mapa=[]
mapa=mapear(mapa,filas)
Bat=int(input())
n=int(input())
for i in range(0,n):
    op=input()
    op,comando=limpiar(op)
    if op=="OP 1":
        print("Bateria:",Bat)
    elif op=="OP 2":
        print("Cargar Bateria")
        b=int(input())
        if Bat+b>100:
            Bat=100
        else:
            Bat+=b
    elif op=="OP 3":
        d=comando[-1]
        print("Robot Apunta a",d)
    elif op=="OP 4":
        ir=comando.split(",")
        x1=int(ir[0].replace("Ir a Posicion (",""))
        y1=int(ir[1].replace(")",""))
        dx=x1-x
        dy=y1-y
        x,Bat=moverse(x,dx,Bat)
        if x==x1:
            y,Bat=moverse(y,dy,Bat)
        print("X:"+str(x))
        print("Y:"+str(y))
    elif op=="OP 5" or op=="OP 6":
        print(comando)
    elif op=="OP 7":
        print(comando)
        nuevomapa=[]
        for i in range(0,len(mapa)):
            if i==(y+1):
                nuevafila=meterpos(mapa[i],x,d)
                nuevomapa.append(nuevafila)
            else:
                nuevomapa.append(mapa[i])
        for i in nuevomapa:
            print(i)
