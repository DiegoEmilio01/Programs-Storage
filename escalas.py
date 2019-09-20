escalas=int(input())
print(escalas)
nvuelos=int(input())
listavuelos=[]
for i in range(0,nvuelos):
    vuelo=input().split(",")
    vuelo=vuelo[:-1]
    if vuelo not in listavuelos:
        listavuelos.append(vuelo)
listalistavuelos=[]
for i in listavuelos:
    lista=[i]
    listalistavuelos.append(lista)
lista=[]
for i in range(0,escalas):
    for vuelos in listalistavuelos:
        ciudad=vuelos[i][1]
        trayecto=[]
        for vuelo in listavuelos:
            if vuelo[0]==ciudad:
                for a in vuelos:
                    trayecto.append(a)
                trayecto.append(vuelo)
        if len(trayecto)>=1:
            lista.append(trayecto)
    listalistavuelos=lista
if len(lista)<1:
    lista=listalistavuelos
print(lista) 
