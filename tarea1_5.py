p=input()
configurar_robot(p)
b=int(input())
v=int(input())
n=int(input())
for i in range(0,n):
    op=input()
    d=obtener_direccion()
    if op=="Op 1":
        print("Bateria:",b)
    elif op=="Op 2":
        print("Cuanto desea cargar?")
        bi=int(input())
        b=b+bi
        if b>100:
            b=100
    elif op=="Op 3":
        print("Velocidad:",v)
    elif op=="Op 4":
        print("Cuanto desea cambiar?")
        vi=int(input())
        if 1<=v+vi<=4:
            v=v+vi
        else:
            print("Velocidad fuera de rango")
    elif op=="Op 5" or op=="Op 9":
        if d=="L":
            girar_izquierda()
        elif d=="R":
            girar_derecha()
        elif d=="U":
            girar_izquierda()
            girar_izquierda()
    elif op=="Op 6" or op=="Op 10":
        if d=="R":
            girar_izquierda()
        elif d=="L":
            girar_derecha()
        elif d=="D":
            girar_izquierda()
            girar_izquierda()
    elif op=="Op 7" or op=="Op 11":
        if d=="D":
            girar_izquierda()
        elif d=="U":
            girar_derecha()
        elif d=="L":
            girar_izquierda()
            girar_izquierda()
    elif op=="Op 8" or op=="Op 12":
        if d=="U":
            girar_izquierda()
        elif d=="D":
            girar_derecha()
        elif d=="R":
            girar_izquierda()
            girar_izquierda()    
    if op=="Op 9" or op=="Op 10"or op=="Op 11"or op=="Op 12":
        m=0
        x=0
        bat=b
        while x<v:
            if b>=5:
                t=avanzar()
                b=b-5
                m+=1
                x+=1
                if t==False:
                    girar_izquierda()
                    girar_izquierda()
                    for k in range(0,m-1):
                        avanzar()
                    girar_izquierda()
                    girar_izquierda()
                    x=v
                    b=bat
                    print("Alerta de Choque")
            else:
                print("Sin bateria")
                x=v
                
m=dibujar_mapa()
print(m)
print("Bateria:",b)
print("Velocidad:",v)

