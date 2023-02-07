#Ejercicio 4

x = 3 
def f():
    y = x + 1 
    print(x)
    
    def g():
        x = 1 
        print(y) 
        print(x)
    g()
    
f()
