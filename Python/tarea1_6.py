p=input()
configurar_robot(p)
b=int(input())
v=int(input())
n=int(input())
for i in range(0,n):
    op=input()
    d=obtener_direccion()    
    if op=="Op 9":
        if d=="D" and b>=v*5:
            m=0
            x=0
            while x<v:
                t=avanzar()
                m+=1
                x+=1
                if t==False:
                    girar_izquierda()
                    girar_izquierda()
                    for k in range(0,m):
                        avanzar()
                    girar_izquierda()
                    girar_izquierda()
                    x=v+1
                    print("Alerta de Choque")
            b=b-5*m
        elif d=="L" and b>=v*5:
            girar_izquierda()
            m=0
            x=0
            while x<v:
                t=avanzar()
                m+=1
                x+=1
                if t==False:
                    girar_izquierda()
                    girar_izquierda()
                    for k in range(0,m):
                        avanzar()
                    girar_izquierda()
                    girar_izquierda()
                    x=v+1
                    print("Alerta de Choque")
        elif d=="R" and b>=v*5:
            girar_derecha()
            m=0
            x=0
            while x<v:
                t=avanzar()
                m+=1
                x+=1
                if t==False:
                    girar_izquierda()
                    girar_izquierda()
                    for k in range(0,m):
                        avanzar()
                    girar_izquierda()
                    girar_izquierda()
                    x=v+1
                    print("Alerta de Choque")
        elif d=="U" and b>=v*5:
            girar_izquierda()
            girar_izquierda()
            m=0
            x=0
            while x<v:
                t=avanzar()
                m+=1
                x+=1
                if t==False:
                    girar_izquierda()
                    girar_izquierda()
                    for k in range(0,m):
                        avanzar()
                    girar_izquierda()
                    girar_izquierda()
                    x=v+1
                    print("Alerta de Choque")
        if b<:
            
            print("Sin bateria")
    if op=="Op 10":
        if d=="U" and b>=v*5:
            m=0
            x=0
            while x<v:
                t=avanzar()
                m+=1
                x+=1
                if t==False:
                    girar_izquierda()
                    girar_izquierda()
                    for k in range(0,m):
                        avanzar()
                    girar_izquierda()
                    girar_izquierda()
                    x=v+1
                    print("Alerta de Choque")
        elif d=="R" and b>=v*5:
            girar_izquierda()
            m=0
            x=0
            while x<v:
                t=avanzar()
                m+=1
                x+=1
                if t==False:
                    girar_izquierda()
                    girar_izquierda()
                    for k in range(0,m):
                        avanzar()
                    girar_izquierda()
                    girar_izquierda()
                    x=v+1
                    print("Alerta de Choque")
        elif d=="L" and b>=v*5:
            girar_derecha()
            m=0
            x=0
            while x<v:
                t=avanzar()
                m+=1
                x+=1
                if t==False:
                    girar_izquierda()
                    girar_izquierda()
                    for k in range(0,m):
                        avanzar()
                    girar_izquierda()
                    girar_izquierda()
                    x=v+1
                    print("Alerta de Choque")
        elif d=="D" and b>=v*5:
            girar_izquierda()
            girar_izquierda()
            m=0
            x=0
            while x<v:
                t=avanzar()
                m+=1
                x+=1
                if t==False:
                    girar_izquierda()
                    girar_izquierda()
                    for k in range(0,m):
                        avanzar()
                    girar_izquierda()
                    girar_izquierda()
                    x=v+1
                    print("Alerta de Choque")
        else:
            print("Sin bateria")
    if op=="Op 11":
        if d=="R" and b>=v*5:
            m=0
            x=0
            while x<v:
                t=avanzar()
                m+=1
                x+=1
                if t==False:
                    girar_izquierda()
                    girar_izquierda()
                    for k in range(0,m):
                        avanzar()
                    girar_izquierda()
                    girar_izquierda()
                    x=v+1
                    print("Alerta de Choque")
        elif d=="D" and b>=v*5:
            girar_izquierda()
            m=0
            x=0
            while x<v:
                t=avanzar()
                m+=1
                x+=1
                if t==False:
                    girar_izquierda()
                    girar_izquierda()
                    for k in range(0,m):
                        avanzar()
                    girar_izquierda()
                    girar_izquierda()
                    x=v+1
                    print("Alerta de Choque")
        elif d=="U" and b>=v*5:
            girar_derecha()
            m=0
            x=0
            while x<v:
                t=avanzar()
                m+=1
                x+=1
                if t==False:
                    girar_izquierda()
                    girar_izquierda()
                    for k in range(0,m):
                        avanzar()
                    girar_izquierda()
                    girar_izquierda()
                    x=v+1
                    print("Alerta de Choque")
        elif d=="L" and b>=v*5:
            girar_izquierda()
            girar_izquierda()
            m=0
            x=0
            while x<v:
                t=avanzar()
                m+=1
                x+=1
                if t==False:
                    girar_izquierda()
                    girar_izquierda()
                    for k in range(0,m):
                        avanzar()
                    girar_izquierda()
                    girar_izquierda()
                    x=v+1
                    print("Alerta de Choque")
        else:
            print("Sin bateria")
    if op=="Op 12":
        if d=="L" and b>=v*5:
            m=0
            x=0
            while x<v:
                t=avanzar()
                m+=1
                x+=1
                if t==False:
                    girar_izquierda()
                    girar_izquierda()
                    for k in range(0,m):
                        avanzar()
                    girar_izquierda()
                    girar_izquierda()
                    x=v+1
                    print("Alerta de Choque")
        elif d=="U" and b>=v*5:
            girar_izquierda()
            m=0
            x=0
            while x<v:
                t=avanzar()
                m+=1
                x+=1
                if t==False:
                    girar_izquierda()
                    girar_izquierda()
                    for k in range(0,m):
                        avanzar()
                    girar_izquierda()
                    girar_izquierda()
                    x=v+1
                    print("Alerta de Choque")
        elif d=="D" and b>=v*5:
            girar_derecha()
            m=0
            x=0
            while x<v:
                t=avanzar()
                m+=1
                x+=1
                if t==False:
                    girar_izquierda()
                    girar_izquierda()
                    for k in range(0,m):
                        avanzar()
                    girar_izquierda()
                    girar_izquierda()
                    x=v+1
                    print("Alerta de Choque")
        elif d=="R" and b>=v*5:
            girar_izquierda()
            girar_izquierda()
            m=0
            x=0
            while x<v:
                t=avanzar()
                m+=1
                x+=1
                if t==False:
                    girar_izquierda()
                    girar_izquierda()
                    for k in range(0,m):
                        avanzar()
                    girar_izquierda()
                    girar_izquierda()
                    x=v+1
                    print("Alerta de Choque")
        else:
            print("Sin bateria")
            
            

m=dibujar_mapa()
print(m)
print("Bateria:",b)
print("Velocidad:",v)
