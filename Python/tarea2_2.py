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
def mapear(mapa,filas,pos,d):
    nfila=int(pos[1])
    ncolumna=int(pos[0])
    for i in range(0,filas):
        f=input()
        f=f.replace("[","|,")
        f=f.replace("]",",|")
        f=f.replace(",","")
        if i==nfila:
            f=meterpos(f,ncolumna,d)
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
d=input()
filas=int(input())
mapa=[]
mapa=mapear(mapa,filas,pos,d)
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
        dir=comando[-1]
        print("Robot Apunta a",dir)
    elif op=="OP 4":
        ir=comando.split(",")
        x=ir[0].replace("Ir a Posicion (","")
        y=ir[1].replace(")","")
        print("X:"+x)
        print("Y:"+y)
    elif op=="OP 5" or op=="OP 6":
        print(comando)
    elif op=="OP 7":
        print(comando)
        for i in mapa:
            print(i)
