lista=input()+" "
n=int(input())
lista1=[]
numero=""
for i in lista:
    if i!=" ":
        numero+=i
    elif i==" ":
        numero=int(numero)
        lista1.append(numero)
        numero=""
lista2=[]
for i in lista1:
    if i<=n:
        lista2.append(i)
print(lista2)
