##definir clases y funciones
def orden_alfabetico(i):
    return i.nombre
class Ingrediente:
    def __init__(self,n,t,p):
        self.nombre=n
        self.tipo=t
        self.puntaje=int(p)
        self.complemento=False
    def __str__(self):
        return self.nombre
class Receta:
    def __init__(self,l,r):
        self.ingredientes=[]
        self.complementos=l
        self.restricciones=r
        self.tipo=[]
    def agregar_ingrediente(self,i):
        res=-1
        for a in self.restricciones:
            if i.tipo==a[0]:
                res=a[1]
        ntipo=0
        for b in self.tipo:
            if i.tipo==b:
                ntipo+=1
        if res!=-1 and ntipo>=res:
            return 2
        elif i in self.ingredientes:
            return 1
        else:
            self.ingredientes.append(i)
            self.tipo.append(i.tipo)
            return 0
    def quitar_ingrediente(self,i):
        if i in self.ingredientes:
            self.ingredientes.remove(i)
            self.tipo.remove(i.tipo)
            return 0
        else:
            return 1
    def calcular_puntaje(self):
        puntos=0
        comp=self.complementos
        for a in self.ingredientes:
            for b in self.ingredientes:
                for c in comp:
                    if (a.nombre!=b.nombre) and (a.nombre in c) and (b.nombre in c):
                        pu=(a.puntaje+b.puntaje)*c[2]
                        comp.remove(c)
                        a.complemento=True
                        b.complemento=True
                        puntos+=pu
            if a.complemento==False:
                puntos+=a.puntaje
        return round(puntos,1)        
##crear lista de ingredientes
caracteres=["|","/",".","_","-",",",";","*"]
caracteres2=["|","/","_","-",",",";","*"]
l=input()+","
palabra=""
lista=[]
for i in l:
    if i in caracteres:
        lista.append(palabra)
        palabra=""
    else:
        palabra+=i
lista_ingredientes=[]
for i in range(0,len(lista)//3):
    pos=i*3
    f=Ingrediente(lista[pos],lista[pos+1],lista[pos+2])
    lista_ingredientes.append(f)
##crear lista de complementos
l=input()+","
palabra=""
lista=[]
for i in l:
    if i in caracteres2:
        lista.append(palabra)
        palabra=""
    else:
        palabra+=i
lista_complementos=[]
for i in range(0,len(lista)//3):
    pos=i*3
    f=[lista[pos],lista[pos+1],float(lista[pos+2])]
    lista_complementos.append(f)
##crear lista de restricciones
n=int(input())
restricciones=[]
for i in range(0,n):
    res=input().split(": ")
    restricciones.append([res[0],int(res[1])])
##crear receta
receta=Receta(lista_complementos,restricciones)
n=int(input())
for i in range(0,n):
    a=input()
    op=a[0]
    ing=a[1:]
    for m in lista_ingredientes:
        if ing==m.nombre:
            ingrediente=m
    if op=="+":
        b=receta.agregar_ingrediente(ingrediente)
        if b==0:
            print("Agregado:",ingrediente)
        elif b==1:
            print("Error:",ingrediente,"ya esta en la receta")
        elif b==2:
            print("Error: no puedes agregar mas ingredientes del tipo",ingrediente.tipo)
    else:
        b=receta.quitar_ingrediente(ingrediente)
        if b==0:
            print("Quitado:",ingrediente)
        elif b==1:
            print("Error:",ingrediente,"no esta en la receta")
##ordenar
receta.ingredientes=sorted(receta.ingredientes,key=orden_alfabetico)

########## NO PUEDES MODIFICAR ESTE CÓDIGO ############
for ingrediente in receta.ingredientes:
	print(ingrediente)
print(receta.calcular_puntaje())
