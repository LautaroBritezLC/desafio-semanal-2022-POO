"""Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url. 
- Url de ejemplo: https://www.jhstoys.com/uploads/6/1/3/7/61377571/s737619424575262359_p1042_i943_w894.jpeg
- Por ratio hacemos referencia por ejemplo a los '16:9' de una imagen de 1920*1080px.

"""
import math
import urllib.request
from PIL import Image as img

def obtenerImg(url, ruta, nombre):
    ruta_Completa = ruta + nombre + '.jpg' #creamos la ruta del archivo
    urllib.request.urlretrieve(url, ruta_Completa) #descargamos la imagen y la almacenamos en la ruta
    return ruta_Completa

ruta = 'C:/Users\polie/Desktop/desafio-semanal-2022-POO/desafio-semanal-2022-POO/src/containers/img/' #donde se guardaran las fotos 
url = input("ingrese la url: ") #el usuario ingresa la url de la imagen
nombre = input("ingrese un nombre para la imagen: ") #le da un nombre para despues ser guardada

imagen = obtenerImg(url,ruta, nombre) #llamamos a la funcion para descargar la imagen

abrirImagen = img.open(imagen) #abrimos la imagen
ancho , alto = abrirImagen.size #obtenemos el alto y el ancho de la imagen
print(f"ancho: {ancho}, alto: {alto}")

mcd = math.gcd(alto,ancho) #calculamos el maximo comun divisor entre el alto y ancho
anchoRelacionAspecto = int(ancho / mcd) #divimos el ancho por el mcd
altoRelacionAspecto = int(alto / mcd) #divimos el alto por el mcd

print(f"la relacion de aspecto (aspect ratio) de la imagen {nombre} es {anchoRelacionAspecto}:{altoRelacionAspecto}")