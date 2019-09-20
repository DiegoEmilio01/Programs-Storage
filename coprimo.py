l=input()
lista=l.split(" ")
listao=[]
largo=len(lista)
for i in range(0,largo):
    num=10**1000
    for a in range(0,len(lista)):
        if int(lista[a])<=num:
            num=int(lista[a])
    lista.remove(str(num))
    listao.append(num)
mcd=1
for i in range(2,listao[0]+1):
    n=0
    for a in listao:
        if a%i==0:
            n+=1
    if n==len(listao):
        mcd=i
if mcd==1:
    print("Coprimo")
elif mcd>1:
    print("No es coprimo. MCD:",mcd)
