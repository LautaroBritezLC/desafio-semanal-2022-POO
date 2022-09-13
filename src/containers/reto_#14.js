class numNarcicista{
    constructor(numero) {
        this.numero = numero;
    }    
    calcularNumNarcisista() {
        let numString = this.numero + ""; //pasamos a string
        let numElevado = 0 //variable para guardar el resultado de elevar el num a la potencia
        let sumaPotencias = 0 //acumulador 
        for (let i = 1; i <= numString.length; i++) { //recorremos de acuerdo a la cantidad de digitos del num
            numElevado= Math.pow(parseInt(numString[i-1]),parseInt(numString.length));//elevamos el primer numero a la cant de digitos que tiene ese numero
            //console.log(`el numero ${numString[i-1]} elevado a ${numString.length} es ${numElevado}`);
            sumaPotencias = sumaPotencias + numElevado; //acumulamos los resultados
            //console.log(`la suma hasta ahora es: ${sumaPotencias}`);
        }
        if (this.numero == sumaPotencias) { //evaluamos si el acumulador es igual al num ingresado
        return `el numero ${this.numero} es un numero armstrong (narcicista)`; 
        }else {
        return `el numero ${this.numero} no es un numero armstrong (narcicista)`;             
        }    
    }
}
let numNarcicista1 = new numNarcicista(153);
console.log(numNarcicista1.calcularNumNarcisista());