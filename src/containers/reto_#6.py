"""Crea un programa que invierta el orden de una cadena de texto sin 
usar funciones propias del lenguaje que lo hagan de forma automática. 
- Si le pasamos 'Hola mundo' nos retornaría 'odnum aloH'"""

palabra = input("ingrese una palabra: ")
listaCompleta = []
palabraLista = list(palabra)

while len(palabraLista)> 0:
    listaCompleta.append(palabraLista[-1])
    palabraLista.pop()    

palabraAlrrevez = "".join(listaCompleta)
print(f"la palabra al revez es: {palabraAlrrevez}")