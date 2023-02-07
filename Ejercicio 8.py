#Ejercicio 8
import random
arch=""
linea=""
i=1

def archivo ():
    
    arch=open("numeros2.txt","w")
    b=""    
    a = ""
    
    for i in range (10):
        n=random.randint (1,10)
        b=str(n)
        arch.write(b+"\n")
    arch.close()
    
    arch=open("numeros2.txt","r")
    lineas=arch.readlines ()
    i=1
    
    for i in range (len(lineas)):
        c=(lineas.count ("5\n"))
    print(c," Coincidencias")    
    arch.close()
   
archivo ()