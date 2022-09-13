class palindromo{
    constructor(oracion) {
        this.oracion = oracion;
    }    
    calcularPalindromo() {
        let oracionMin = this.oracion.toLowerCase() //pasamos la oracion a minuscula
        let oracionEspacio = oracionMin.split("").filter(i => i != " ").join(""); //transformamos en lista y eliminamos los espacios en blanco y volvemos a transformar en string
        let oracionReverse = oracionEspacio.split("").reverse().join(""); //transformamos en lista y usamos reverse para dar vuelta la cadena y volvemos a tranformar en string

        if (oracionEspacio == oracionReverse) {
            return`la oracion ${this.oracion} es palindromo`;
        }else{
            return `la oracion ${this.oracion} no es palindromo`;
        }         
    }
}
let Objpalindromo = new palindromo("arriba la birra");
console.log(Objpalindromo.calcularPalindromo());