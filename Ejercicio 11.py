#Ejercicio 11
import random
arch=""
linea=""
i=1

def archivo ():
    
    arch=open("ejercicio11.txt","w")
    b=""    
    a = ""
    c=int(input("Por favor, ingrese número de inicio: "))
    f=int(input("Por favor, ingrese número de finalización: "))
    
    for i in range (250):
        n=random.randint (c,f)
        b=str(n)
        arch.write(b+"\n")
    arch.close()
    
archivo ()