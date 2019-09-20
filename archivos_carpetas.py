import os
import shutil

print(os.getcwd())
print(os.listdir("."))

#no se puede crear un archivo que ya existe
os.rmdir("PRUEBA")
#da error si no esta el archivo
#os.mkdir("PRUEBA2")
#archivo=open("C:/Users/Diego/AppData/Local/Programs/Python/Python37-32/Amigo_Secreto/prueba5.txt","w")
#archivo.close()
#shutil.move("prueba2.txt",r"C:\Users\Diego\AppData\Local\Programs\Python\Python37-32\Amigo_Secreto")
