a=int(input())
def primo(a):
    c=2
    pri=True
    while c<a and pri:
        if a%c==0:
            pri=False
        c+=1
    return(pri)
b=0
d=2
while b<a:
    p=primo(d)
    if p:
        print(d)
        b+=1
    d+=1
