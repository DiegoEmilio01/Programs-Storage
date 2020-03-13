frase=input()
feditada=frase
for i in frase:
    if i!="a" and i!="e" and i!="i" and i!="o" and i!="u" and i!=" " and i!="A" and i!="E" and i!="I" and i!="O" and i!="U":
        feditada=feditada.replace(i,"")
print(feditada)
