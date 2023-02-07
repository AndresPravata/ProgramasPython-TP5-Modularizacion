#Ejercicio 7

i=1

arch=""
linea=""

def archivo ():
    
    arch=open("colores.txt","w")
    
    
    a = ""
    for i in range (5):
        a = input("ingrese un color ")
        arch.write(a+"\n")
  
    arch.close ()
  
archivo ()

