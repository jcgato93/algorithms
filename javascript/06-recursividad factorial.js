// ciclo for
var factorial = function(n) {
    var result = 1;    
    for(var i = 0; i <= n-1; i++) {
        result = result * (n-i);
    }
    return result;
};

console.log("The value of 5! should be " + 5*4*3*2*1);
console.log("The value of 5! is " + factorial(5));
console.log("The value of 0! should be 1");
console.log("The value of 0! is " + factorial(0));


// funcion recursiva
var factorialRecursivo = function(n) {
	// base case: 
	if (n === 0) {
        return 1;
    }
	// recursive case:
	return  n * factorialRecursivo(n-1);
}; 

console.log("The value of 0! is " + factorialRecursivo(0) + ".");
console.log("The value of 5! is " + factorialRecursivo(5) + ".");