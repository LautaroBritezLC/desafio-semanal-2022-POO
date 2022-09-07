llaves = {
    "(" : ")",
    "[" : "]",
    "{" : "}",
}
def exprecionBalanceada(expresion):
    #lista para las llaves
    expresionPar = []
    #creamos un diccionario invertido
    invertirPar = {value: key for key, value in llaves.items()}
    #variable para saber si una expresion esta balanceada
    balanceado = True
    for letra in expresion:
        #verifica si la letra es una llave que se abre y lo agrega a la lista
        if letra in llaves.keys():
            expresionPar.append(letra)

        #Si la lista esta dentro de los simbolos de cierra y coincide con el ultimo valor de la lista, lo elimina
        elif letra in llaves.values() and invertirPar[letra] == expresionPar[-1]:
            #print("letra ---",letra)
            #print("inverPar --",invertirPar[letra])
            #print("exprePar --",expresionPar[-1])
            expresionPar.pop()

        #si la letra esta en los simbolos de cierre, y no se abrio antes, entonces no esta balanceada
        elif letra in llaves.values():
            balanceado = False

    #si hay valores en la lista, la expresion no esta balanceada
    if len(expresionPar) > 0:
        balanceado = False

    if balanceado == True:
        print(f"la expresion:{expresion} esta balanceada")
    else:
        print(f"la expresion:{expresion} no esta balanceada")

expresion = input("ingrese una expresion: ")
exprecionBalanceada(expresion)