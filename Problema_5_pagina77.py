"""Într-un fişier sunt înscrise caractere arbitrare. Elaboraţi un program care afişează pe ecran numărul vocalelor din fişier."""
with open ("D:\Pentru studiu\python\Problema_5_pagina77.txt", "r") as f:
    text=f.read()

vocale=[]
nr_de_vocale=0
for i in range(0,len(text)):
    if text[i]=="a" or text[i]=="e" or text[i]=="i" or text[i]=="o" or text[i]=="u" or text[i]=="A" or text[i]=="E" or text[i]=="I" or text[i]=="O" or text[i]=="U":
        nr_de_vocale+=1 
        vocale.extend(text[i])

print("numarul de vocale este:",nr_de_vocale,"\n","Vocalele sunt:",vocale)