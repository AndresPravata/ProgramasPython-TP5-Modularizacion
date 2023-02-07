#Ejercicio 6

arch=""
linea=""
i=1

def archivo ():
    
    arch=open("numeros.txt","w")
    b=""    
    a = ""
    for i in range (10):
        a = int(input("ingrese un número: "))
        b=str(a)
        
        arch.write(b+"\n")
        
    arch.close()
   
archivo ()