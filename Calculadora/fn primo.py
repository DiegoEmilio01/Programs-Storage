a=int(input())
def primo(a):
    c=2
    pri=True
    while c<a and pri:
        if a%c==0:
            pri=False
        c+=1
    return(pri)
c=primo(a)
print(c)
