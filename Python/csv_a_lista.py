archivo = open("data-cruda.csv","r")
lineas=archivo.readlines()
archivonuevo=open("data_en_lista.txt","w")
lista=[]
for i in lineas:
      elemento=i.strip().split(",")
      lista.append(elemento)
print(lista,file=archivonuevo)
archivonuevo.close()
archivo.close()
