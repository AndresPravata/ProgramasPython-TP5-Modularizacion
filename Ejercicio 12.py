#Ejercicio 12

n = int(input("Por favor, ingrese el ancho del rectángulo: "))
m = int(input("Por favor, ingrese la altura del rectángulo: "))

for f in range (1,m+1):
    for c in range (1,n+1):
        
        #print("#", end="")
        
        if (f > 1) and (f < n) and (c > 1) and c < m:
            
            print(" ",)
        else:
            print("#", end="")
            
     
    #print("#")
    #if (f > 1) and (f < m) and (c > 1) and c < n:
    #    print(" ")
        
     
    #print(" ")
        
        
        
       # if (f > 1) and (f < m) and (c > 1) and c < n:
            
        #    print (" ")
            
            
        #else:
            
             #print("#", end="")                 
        
        
        
