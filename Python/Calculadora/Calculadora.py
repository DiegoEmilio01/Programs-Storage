def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
def subfactorial(n):
    if n==0:
        return 1
    elif n<3:
        return n-1
    else:
        return (n-1)*(subfactorial(n-1)+subfactorial(n-2))
def exp(n):
    x=1
    i=0
    suma=0
    while abs(x)>=(10**-10):
        x=(n**i)/factorial(i)
        suma+=x
        i+=1
    return suma
def sen(n):
    n=n*3.1415926535897932/180
    x=1
    i=0
    suma=0
    while abs(x)>=(10**-10):
        x=((-1)**i)*(n**(2*i+1))/factorial(2*i+1)
        suma+=x
        i+=1
    return suma
def cos(n):
    n=n*3.1415926535897932/180
    x=1
    i=0
    suma=0
    while abs(x)>=(10**-10):
        x=((-1)**i)*(n**(2*i))/factorial(2*i)
        suma+=x
        i+=1
    return suma
def ln(n):
    x=1
    n=(n-1)/(n+1)
    i=0
    suma=0
    while abs(x)>=(10**-10):
        x=(n**(2*i+1))/(2*i+1)
        suma+=x
        i+=1
    return suma*2
def log(argumento,base):
    return ln(argumento)/ln(base)
def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)
def tg(n):
    return sen(n)/cos(n)
s=input("Operaciones disponibles: +, -, *, /, ^, exp(n), sen(n), cos(n), tg(n), ln(n), (base)log(argumento), n!, !n, fibonacci(n).\nIngrese cálculos:")+";"
lista=[]
ops=["+","-","*","/","^",";"]
palabra=""
for i in s:
    if i in ops:
        lista.append(palabra)
        palabra=""
        if i!=";":
            lista.append(i)
    else:
        palabra+=i
#print("".join(lista))
lista_funciones_hechas=[]
for i in lista:
    if "exp" in i:
        lista_funciones_hechas.append(exp(float(i[4:-1])))
    elif "sen" in i:
        lista_funciones_hechas.append(sen(float(i[4:-1])))
    elif "cos" in i:
        lista_funciones_hechas.append(cos(float(i[4:-1])))
    elif "tg" in i:
        lista_funciones_hechas.append(tg(float(i[3:-1])))
    elif "ln" in i:
        lista_funciones_hechas.append(ln(float(i[3:-1])))
    elif "log" in i:
        a=i.split(")log(")
        lista_funciones_hechas.append(log(float(a[1][:-1]),float(a[0][1:])))
    elif "fib" in i:
        lista_funciones_hechas.append(fibonacci(float(i[10:-1])))
    elif "!"==i[0]:
        lista_funciones_hechas.append(subfactorial(float(i[1:])))
    elif "!"==i[-1]:
        lista_funciones_hechas.append(factorial(float(i[:-1])))
    else:
        if i in ops:
            lista_funciones_hechas.append(i)
        else:
            lista_funciones_hechas.append(float(i))
lista_funciones_hechas.append(";")
#print(lista_funciones_hechas)
ops_presentes=[False,False,False,False,False]
if "+" in lista_funciones_hechas:
    ops_presentes[0]=True
if "-" in lista_funciones_hechas:
    ops_presentes[1]=True
if "*" in lista_funciones_hechas:
    ops_presentes[2]=True
if "/" in lista_funciones_hechas:
    ops_presentes[3]=True
if "^" in lista_funciones_hechas:
    ops_presentes[4]=True
i=len(lista_funciones_hechas)-1
while 0<=i and ops_presentes[4]:
    if lista_funciones_hechas[i]=="^":
        lista_funciones_hechas=lista_funciones_hechas[:i-1]+[lista_funciones_hechas[i-1]**lista_funciones_hechas[i+1]]+lista_funciones_hechas[i+2:]
        i=i-1
    i+=-1
i=0
while i<len(lista_funciones_hechas) and ops_presentes[2]:
    if lista_funciones_hechas[i]=="*":
        lista_funciones_hechas=lista_funciones_hechas[:i-1]+[lista_funciones_hechas[i-1]*lista_funciones_hechas[i+1]]+lista_funciones_hechas[i+2:]
        i=i-1
    i+=1
i=0
while i<len(lista_funciones_hechas) and ops_presentes[3]:
    if lista_funciones_hechas[i]=="/":
        lista_funciones_hechas=lista_funciones_hechas[:i-1]+[lista_funciones_hechas[i-1]/lista_funciones_hechas[i+1]]+lista_funciones_hechas[i+2:]
        i=i-1
    i+=1
i=0
while i<len(lista_funciones_hechas) and ops_presentes[0]:
    if lista_funciones_hechas[i]=="+":
        lista_funciones_hechas=lista_funciones_hechas[:i-1]+[lista_funciones_hechas[i-1]+lista_funciones_hechas[i+1]]+lista_funciones_hechas[i+2:]
        i=i-1
    i+=1
i=0
while i<len(lista_funciones_hechas) and ops_presentes[1]:
    if lista_funciones_hechas[i]=="-":
        lista_funciones_hechas=lista_funciones_hechas[:i-1]+[lista_funciones_hechas[i-1]-lista_funciones_hechas[i+1]]+lista_funciones_hechas[i+2:]
        i=i-1
    i+=1
print(lista_funciones_hechas[0])
