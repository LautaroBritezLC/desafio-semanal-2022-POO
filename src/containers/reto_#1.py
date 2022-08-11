def fnAnagrama(palabra1,palabra2):
    if palabra1.isalpha() == True and palabra2.isalpha() == True:
        if palabra1 != palabra2:
            palabra1 = palabra1.lower()
            palabra2 = palabra2.lower()

            listPalabra1 = list(palabra1)
            listPalabra2 = list(palabra2)

            listPalabra1.sort()
            listPalabra2.sort()

            return(set(listPalabra1) == set(listPalabra2))
        else:
            return False
    else:
        msg = "por favor ingrese una palabra"
        return msg

print("funcion que calcula si dos palabras son anagramas: ")

palabra1 = input("ingrese una palabra: ")
palabra2 = input("ingrese otra palabra: ")

es_Anagrama = fnAnagrama(palabra1, palabra2)

if es_Anagrama == True:
    print(f"{palabra1} es anagrama de {palabra2}")
elif es_Anagrama == False:
    print(f"{palabra1}  no es anagrama de {palabra2}")
else:
    print(es_Anagrama)

