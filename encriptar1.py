def dig(a):
    n=0
    p=""
    for i in a:
        n=n+1
    for i in a:
        d=int(i)*n
        l=str(d)
        m=l[0]
        p=p+m
    g=int(p)
    return g
        
    
b=input()
n=dig(b)
print(n)
