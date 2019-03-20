archivo=open("ejemplo_archivos.txt","w")
print('archivo=open("ejemplo_archivos.txt","w")\nprint("hola",file=archivo)\narchivo.close()\narchivonuevo=open("ejemplo_archivos.txt")\nfrase=archivonuevo.readlines()\narchivonuevo.close()\nprint(frase)\nfor i in frase:\n\tlimpio=i.strip()\n\tprint(limpio)',file=archivo)
archivo.close()
archivonuevo=open("ejemplo_archivos.txt")
frase=archivonuevo.readlines()
archivonuevo.close()
for i in frase:
    limpio=i.strip()
    print(limpio)

## Para .csv usar i.strip().split(",") y se obtiene otra lista.
