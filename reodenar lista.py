lista=input().split(" ")
listao=[]
largo=len(lista)
for i in range(0,largo):
    num=10**1000
    for a in range(0,len(lista)):
        if int(lista[a])<=num:
            num=int(lista[a])
    lista.remove(str(num))
    listao.append(num)
print(listao)
