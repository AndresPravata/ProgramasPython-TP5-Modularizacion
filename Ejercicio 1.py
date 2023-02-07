#Ejercicio 1

def cuadrado (a):
    b=locals()
    b=a
    c=locals()
    d=locals()
    print (a, "elevado al cuadrado es: ", b**2) 

a=int(input("Por favor, Ingrese un número "))
cuadrado (a)
