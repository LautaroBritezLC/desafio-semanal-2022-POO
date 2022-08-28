"""Crea un programa que cuente cuantas veces se repite cada palabra 
y que muestre el recuento final de todas ellas. 
- Los signos de puntuación no forman parte de la palabra. 
- Una palabra es la misma aunque aparezca en mayúsculas y minúsculas. 
- No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente."""

oracion = input("ingrese una oracion: ")
oracion = oracion.lower()
listaOracion = oracion.split(" ")
cont = 1
listaNueva = {}

for palabra in listaOracion:
    if palabra in listaNueva:
        listaNueva[palabra] += 1
    else:
        listaNueva[palabra] = 1

for palabra in listaNueva:
    repeticionPalabra = listaNueva[palabra]
    print(f"la palabra {palabra} se repitio {repeticionPalabra} veces")