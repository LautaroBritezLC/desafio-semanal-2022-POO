function factorial(num) {
    if (num <= 1) return 1; //si el numero ingresado es 1 retornamos 1
    return  num * factorial(num - 1); //si es mayor a 1 multiplicamos el num por lo que retorno la funcion
}
console.log("El factorial es: " + factorial(5))