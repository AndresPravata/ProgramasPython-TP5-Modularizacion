#Ejercicio 10
import random
arch=""
linea=""
i=1

def archivo ():
    
    arch=open("ejercicio10.txt","w")
    b=""    
    a = ""
    
    for i in range (250):
        n=random.randint (1,100)
        b=str(n)
        arch.write(b+"\n")
    arch.close()
    
archivo ()