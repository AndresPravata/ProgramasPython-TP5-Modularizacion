#Ejercicio 13

import math

decimal=0
resto=0
binario=[]
i=1
b=0
c=0
      
decimal=int(input("Por favor, Ingrese un número "))

while (decimal>1):
    resto=decimal%2
    binario.append (resto)
    decimal=decimal//2

binario.insert (0,decimal)



c=int(''.join(binario))
#for i in range (len(binario)):
    #c=int(join.binario [i])
    

#a=len(binario)

#for a in range (i):
#b=int(binario [])
        
print ("El número en binario es: ", c)