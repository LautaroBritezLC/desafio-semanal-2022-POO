codigoMorseDic = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "ñ": "--.--",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    '"': ".-..-.",
    "/": "-..-.",
    " ": "/"
}


def traductorMorse (oracion : str): 
    #string que mostraremos
    textoEnMorse = ""

    for letra in oracion.lower():
        #obtiene la traduccion de la letra, si no existe retorna none
        letraMorse = codigoMorseDic.get(letra)
        textoEnMorse += f"{letraMorse}"

    print(f"la oracion {oracion} en morse es: {textoEnMorse}")


def traductorTextoNatural (oracionMorse : str):
    #string que mostraremos
    textoNatural = "" 
    #invertimos los valores y las llaves y creamos un nuevo diccionario   
    textoNaturalDic = {valor: llave for llave, valor in codigoMorseDic.items()}

    #Separa en palabras unicas
    for palabra in oracionMorse.split("   "):
        #cada palabra por separado
        for letrMorse in palabra.split():
            #intenta obtener la letra del diccionario
            letraNatural = textoNaturalDic.get(letrMorse)
            #print(letraNatural , "/" ,letrMorse)

            #si no existe la letra, lo marca con un *
            if letraNatural is None:
                textoNatural += "*"
            #en caso contrario, añade la letra traducida a la cadena
            else:
                textoNatural += letraNatural
        #añade un espacio al final de la palabra
        textoNatural += " "


    print(f"El codigo morse ({oracionMorse}) en texto natural es: {textoNatural}")


#oracion = input("ingrese una oracion")
#traductorMorse(oracion)

#oracionMorse = input("ingrese codigo morse: ")
#traductorTextoNatural(oracionMorse)

def morseTraductor(frase: str):
    esMorse = False
    #si alguna de letras de la frase esta en los valores del diccionario morse, lo traducira a texto natural
    #en caso contrario, lo traduce a morse
    for letra in frase.lower().split():
        print(letra)
        if letra in codigoMorseDic.values():
            esMorse = True


    if esMorse:
        traductorTextoNatural(frase)
    else:
        traductorMorse(frase.lower())

frase = input("ingrese una frase o codigo morse: ")
morseTraductor(frase)