#Ejercicio 9
import random
arch=""
linea=""
i=1

def archivo ():
    
    arch=open("numeros3.txt","w")
    b=""    
    a=""
    
    for i in range (10):
        n=random.randint (1,10)
        b=str(n)
        arch.write(b+"\n")
    arch.close()
    
    arch=open("numeros3.txt","r")
    lineas=arch.readlines ()
    i=1
    c=0
    d=0
    
    for i in range (len(lineas)):
        lineas [i]=lineas [i].rstrip("\n")
        c=int(lineas [i])
        d=d+c

    print ("La suma de los números del archivo es: ",d)  
    print ("El promedio es: ",(d/10))      
        
    arch.close()
   
archivo ()