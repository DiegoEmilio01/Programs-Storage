def subfactorial(n):
    if n==0:
        return 1
    elif n<3:
        return n-1
    else:
        return (n-1)*(subfactorial(n-1)+subfactorial(n-2))
n=int(input())
lista=[]
for i in range(0,n):
    lista.append(subfactorial(i))
print(lista)
