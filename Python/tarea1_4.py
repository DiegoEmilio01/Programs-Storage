p=input()
configurar_robot(p)
b=int(input())
v=int(input())
n=int(input())
for i in range(0,n):
    op=input()
    d=obtener_direccion()    
    if op=="Op 9":
        if d=="L":
            girar_izquierda()
        elif d=="R":
            girar_derecha()
        elif d=="U":
            girar_izquierda()
            girar_izquierda()
    elif op=="Op 10":
        if d=="R":
            girar_izquierda()
        elif d=="L":
            girar_derecha()
        elif d=="D":
            girar_izquierda()
            girar_izquierda()
    elif op=="Op 11":
        if d=="D":
            girar_izquierda()
        elif d=="U":
            girar_derecha()
        elif d=="L":
            girar_izquierda()
            girar_izquierda()
    elif op=="Op 12":
        if d=="U":
            girar_izquierda()
        elif d=="D":
            girar_derecha()
        elif d=="R":
            girar_izquierda()
            girar_izquierda()
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
                
