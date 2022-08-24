"""Crea una única función (importante que sólo sea una) 
que sea capaz de calcular y retornar el área de un polígono. 

- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
"""

from math import pi, tan

def fnAreaPoligono(poligono):
    poligono = int(poligono)
    if poligono == 1:
        medLado = float(input("ingrese la medida de los lados: "))
        area = 3 * medLado**2 / (4 * tan(pi/3)) 
        area = round(area, 3)

    elif poligono == 2:
        medLado = float(input("ingrese la medida de los lados: "))
        area = 4 * medLado**2 / (4 * tan(pi/4))
        area = round(area, 3)

    else:
        base = float(input("ingrese la medida de la base: "))
        altura = float(input("ingrese la medida de la altura: "))  
        area =  base * altura
    return area          

print("bienvenido a la calculadora del area de un poligono")
print("Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.")
print("-----------------------------------------------------------------")
poligono = input("ingrese el poligono que desea calcular --> Triángulo(pulse 1)/Cuadrado(pulse 2)/Rectángulo(pulse 3)")

while poligono.isalpha() == True or poligono != "1" and poligono != "2" and poligono != "3":
        print("por favor ingrese uno de los valores mostrados")
        poligono = input("ingrese el poligono que desea calcular --> Triángulo(pulse 1)/Cuadrado(pulse 2)/Rectángulo(pulse 3)")

if poligono == "1":
        print(f"el area del triangulo es: {fnAreaPoligono(poligono)} cm²")    
elif poligono == "2":
        print(f"el area del cuadrado es: {fnAreaPoligono(poligono)} cm²")   
else:
        print(f"el area del rectangulo es: {fnAreaPoligono(poligono)} cm²")     
