def decodificar(f):
    n=0
    f=f+" "
    cod=""
    for i in f:
        unica=False
        if i==" ":
            break
        if f[n+1]!="2" and f[n+1]!="3" and f[n+1]!="4" and f[n+1]!="5" and f[n+1]!="6" and f[n+1]!="7" and f[n+1]!="8" and f[n+1]!="9":
            unica=True
        if i!="2" and i!="3" and i!="4" and i!="5" and i!="6" and i!="7" and i!="8" and i!="9" and unica:
            cod+=i
        elif i!="2" and i!="3" and i!="4" and i!="5" and i!="6" and i!="7" and i!="8" and i!="9":
            l=i*int(f[n+1])
            cod+=l
        n+=1
    return(cod)

def codificar(f):
    n=0
    f=f+" "
    cod=""
    nl=0
    for i in f:
        nl+=1
        if i==" ":
            break
        if i!=f[n+1]:
            cod+=i
            if nl>1:
                p=str(nl)
                cod+=p
            nl=0
        n+=1
    return(cod)

string = input()
funcion = input()
if funcion == 'decodificar':
    print(decodificar(string))
else:
    print(codificar(string))
