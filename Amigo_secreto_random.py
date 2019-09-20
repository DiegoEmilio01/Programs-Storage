# no se regalan a si mismos y no le regalan al que les toco
import random
def amigo_secreto(lista, l, sol, soluciones):
    if len(sol) == len(lista):
        copia=sol.copy()
        soluciones.append(copia)
        return True
    else:
        persona=lista[len(sol)]
        posibles=posi(persona,l,sol)
        terminado=False
        lista_indices=[]
        while (len(lista_indices)<len(posibles)) and (not terminado):
            i=-2
            while i==-2:
                i=random.randint(0,len(posibles)-1)
                if i in lista_indices:
                    i==-2
            lista_indices.append(i)
            amigo=posibles[i]
            sol.append([persona,amigo])
            l.remove(amigo)
            terminado=amigo_secreto(lista,l,sol,soluciones)
            sol.remove([persona,amigo])
            l.append(amigo)
            i+=1
        return terminado
def posi(persona,l,sol):
    posibles=[]
    for i in l:
            if  i!=persona and ([i,persona] not in sol):
                posibles.append(i)
    return posibles
def resolver(lista):
    soluciones=[]
    l=lista.copy()
    sol=[]
    amigo_secreto(l,lista,sol,soluciones)
    return soluciones
def orden_alfabetico(i):
    return i
def orden_lista(i):
    return i[0]
lista_nombres=input("Escriba la lista de amigos separados por ',' a contonuación: ").split(", ")
if len(lista_nombres)>2:
    soluciones=resolver(lista_nombres)
    solucion=sorted(soluciones[0],key=orden_lista)
    lista_nombres=sorted(lista_nombres,key=orden_alfabetico)
    print(solucion)
#escribir archivos
    for i in range(0,len(lista_nombres)):
        archivo=open("C:/Users/Diego/AppData/Local/Programs/Python/Python37-32/Amigo_Secreto/"+lista_nombres[i]+".txt","w")
        print(solucion[i][0]+" te toco regalarle a "+solucion[i][1]+".",file=archivo)
        archivo.close()
elif len(lista_nombres)==2:
    print(lista_nombres[0],"le regala a",lista_nombres[1],"y",lista_nombres[1],"le regala a",lista_nombres[0]+" ¡Que fome!")
else:
    print("No se puede jugar solo.")
