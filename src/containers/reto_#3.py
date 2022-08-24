"""Escribe un programa que se encargue de comprobar si un número es o no primo. 
    Hecho esto, imprime los números primos entre 1 y 100.
    
    """
def fnNumeroPrimos():
    for i in range(1,101):
        if i > 1:
            for h in range(2,i):
                if(i % h == 0):
                    break
            else:
                print(i)
                print("---")
fnNumeroPrimos()    