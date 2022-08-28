"""Crea un programa se encargue de transformar un número decimal a binario 
sin utilizar funciones propias del lenguaje que lo hagan directamente."""
numeroDecimal = int(input("ingrese un numero: "))
listaBinario = []
def fnCalcularBinario(numeroDecimal):
    residuo = 1
    while numeroDecimal > residuo:
        div = numeroDecimal / 2
        residuo = int(numeroDecimal%2)
        print(f"{numeroDecimal}/2 = {div} --el resto es: {residuo}")
        numeroDecimal = div
        listaBinario.append(residuo)

    invertir = listaBinario[::-1]
    binario = str(invertir)
    binario = binario.replace(",", "")
    print("----------------------------------------------------------------------------")
    return binario

print(f"el numero {numeroDecimal} en binario es: {fnCalcularBinario(numeroDecimal)}")
