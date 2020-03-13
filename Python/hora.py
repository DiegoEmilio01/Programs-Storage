n=int(input())
h=int(input())
m=int(input())
d=(h*100+m)
g=(h%1000)
print(g)
if 0<=d<=820:
    print("CONTESTAR")
elif 820<d<1300 and g==909:
    print("CONTESTAR")
elif 1300<=d<=1950 and (h//100000)!=877:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
