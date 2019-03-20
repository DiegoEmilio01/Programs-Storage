import random
def amigo_secreto(lista,l,sol,soluciones):
    if len(sol)==len(lista):
        copia=sol.copy()
        soluciones.append(copia)
        if len(soluciones)==8000:
            return True
        return False
    else:
        persona=lista[len(sol)]
        posible=[]
        for i in l:
            if (i not in sol) and i!=persona and ([i,persona] not in sol):
                posible.append(i)
        i=0
        terminado=False
        while (i<len(posible)) and (not terminado):
            amigo=posible[i]
            sol.append([persona,amigo])
            l.remove(amigo)
            terminado=amigo_secreto(lista,l,sol,soluciones)
            sol.remove([persona,amigo])
            l.append(amigo)
            i+=1
        return terminado
def resolver(lista):
    soluciones=[]
    l=lista.copy()
    sol=[]
    amigo_secreto(l,lista,sol,soluciones)
    return soluciones
lista=input().split(" ")
soluciones=resolver(lista)
a=random.randint(0,len(soluciones)-1)
print(soluciones[a])
##no se regalan a si mismos y no le regalan al que les toco
