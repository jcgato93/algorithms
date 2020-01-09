# Ordenamiento 

Ordenar una lista de elementos en orden ascendente o descendente puede ayudarle a un ser humano o a una computadora a encontrar elementos rápidamente en esa lista, tal vez al usar un algoritmo como una búsqueda binaria. JavaScript tiene un método integrado de ordenamiento. Funciona en arreglos de números, o incluso en arreglos de cadenas:

```javascript
var animals = ["gnu", "zebra", "antelope", "aardvark", "yak", "iguana"];
animals.sort();
console.log(animals);
//["aardvark", "antelope", "gnu", "iguana", "yak", "zebra"]
```


Un paso clave en muchos algoritmos de ordenamiento (incluyendo el ordenamiento por selección) es intercambiar la ubicación de dos elementos en un arreglo
```javascript
var swap = function(array, firstIndex, secondIndex) {
    var temp = array[firstIndex];
	array[firstIndex] = array[secondIndex];
	array[secondIndex] = temp;
};

var testArray = [7, 9, 4];
swap(testArray, 0, 1);

console.log(testArray);
```
