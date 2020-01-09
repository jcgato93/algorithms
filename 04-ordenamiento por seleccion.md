# Ordenamiento por seleccion (selection sort)

Hay muchas diferentes maneras de ordenar. Aquí hay una sencilla, llamada ordenamiento por selección

1. Encuentra el valor más bajo. Intercambialo con el valor del primer indice.

2. Encuentra el segundo valor más bajo. Intercámbiala con el segundo indice.

3. Repetir hasta que el arreglo este ordenado.

Este algoritmo se llama ordenamiento por selección porque selecciona repetidamente el siguiente elemento más bajo y lo intercambia a su lugar.

```javascript
var swap = function(array, firstIndex, secondIndex) {
    var temp = array[firstIndex];
    array[firstIndex] = array[secondIndex];
    array[secondIndex] = temp;
};

var indexOfMinimum = function(array, startIndex) {

    var minValue = array[startIndex];
    var minIndex = startIndex;

    for(var i = minIndex + 1; i < array.length; i++) {
        if(array[i] < minValue) {
            minIndex = i;
            minValue = array[i];
        }
    } 
    return minIndex;
}; 

var selectionSort = function(array) {    
    var index;
    for(var i= 0; i < array.length; i++) {
        index = indexOfMinimum(array, i);
        swap(array,i, index);

        // simulation
        console.log(array)
    }
};

var array = [22, 11, 99, 88, 9, 7, 42];
selectionSort(array);
console.log("Array after sorting:  " + array);
```


```python
def selection_sort(arr, simulation=False):
    """ Selection Sort
        Complexity: O(n^2)
    """
    iteration = 0
    if simulation:
        print("iteration",iteration,":",*arr)
        
    for i in range(len(arr)):
        minimum = i
        
        for j in range(i + 1, len(arr)):
            # "Select" the correct value
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum], arr[i] = arr[i], arr[minimum]
        
        if simulation:
                iteration = iteration + 1
                print("iteration",iteration,":",*arr)
            
    return arr

if __name__ == "__main__":
    array = [22, 11, 99, 88, 9, 7, 42]
    selection_sort(array,True)    
```