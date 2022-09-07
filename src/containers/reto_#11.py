"""Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e 
imprima otras dos cadenas como salida (out1, out2). - out1 contendrá todos los caracteres 
presentes en la str1 pero NO estén presentes en str2. - 
out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1."""

cadena1 = input("ingrese una cadena: ")
cadena2 = input("ingrese 2da cadena cadena:")

def invertirCadenas(cadena1,cadena2):
    Out1 = ""
    Out2 = ""

    for letra in cadena1:
        if not letra in cadena2:
            Out1 += f"{letra}"

    for letra in cadena2:
        if not letra in cadena1:
            Out2 += f"{letra}"

    print(f"los caracteres presentes en el str1 pero no estan presentes en el str2 son: {Out1}")
    print(f"los caracteres presentes en el str2 pero no estan presentes en el str1 son: {Out2}")    

invertirCadenas(cadena1,cadena2)
