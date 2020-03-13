Bat=int(input())
n=int(input())
for i in range(0,n):
    op=input()
    if "OP 1" in op:
        print("Bateria:",Bat)
    elif "OP 2" in op:
        print("Cargar Bateria")
        b=int(input())
        if Bat+b>100:
            Bat=100
        else:
            Bat+=b
    elif "OP 3" in op:
        if "R" in op:
            d="R"
        elif "L" in op:
            d="L"
        elif "D" in op:
            d="D"
        elif "U" in op:
            d="U"
        print("Robot Apunta a",d)
    elif "OP 4" in op:
        op=op.replace("OP 4","")
        lis=op.split("(")
        pos=lis[1].split(",")
        x=pos[0]
        y=pos[1].replace(")","")
        print("X:"+x)
        print("Y:"+y)
    elif "OP 5" in op:
        print("Deshacer Movimiento")
    elif "OP 6" in op:
        print("Rehacer Movimiento")
    elif "OP 7" in op:
        print("Mostrar Mapa")
