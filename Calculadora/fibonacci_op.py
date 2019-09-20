def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input())
lista=[]
for i in range(0,n):
    lista.append(fibonacci(i))
print(lista)
