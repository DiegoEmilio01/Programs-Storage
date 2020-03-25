class Ingrediente:
    def __init__(self,n,t,p):
        self.nombre=n
        self.tipo=t
        self.puntaje=int(p)
    def __str__(self):
        return self.nombre
class Receta:
    def __init__(self):
        self.ingredientes=[]
i=Ingrediente("manzana","fruta","1")
lista=[i]
if i in lista:
    print(True)
else:
    print(False)

