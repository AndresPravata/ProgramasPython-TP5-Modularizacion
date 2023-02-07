#Ejercicio 5

arch=""
linea=""

def archivo ():
    
    arch=open("palabras.txt","r")
    
    print (arch.read ())  
    arch.close()
   
archivo ()

