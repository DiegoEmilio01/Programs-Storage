archivo = open("data-cruda.txt","r")
lineas=archivo.readlines()
print(lineas)
archivonuevo=open("data_en_listas.txt","w")
for i in lineas:
      elemento=i.strip().split(",")
      print(elemento,file=archivonuevo)
archivonuevo.close()
archivo.close()
# Para .csv usar i.strip().split(",") y se obtiene otra lista.
