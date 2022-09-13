class factorialRecursivo{
    constructor(numeroFact) {
        this.numeroFact = numeroFact;
    }
    
    calcularFactorial() {
        let fact = this.numeroFact
        if (fact < 0) {
            return "no se puede calcular el factorial de un numero negativo"
        }
        else if (fact <= 1){
            return 1
        }
        else {
            console.log(fact * calcularFactorial(fact-1))
        }
    }
}

let factorial = new factorialRecursivo(4);
console.log(factorial.calcularFactorial());

//No anda nose si es porque en POO no me deja llamar a la misma funcion