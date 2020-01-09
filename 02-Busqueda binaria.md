# Busqueda binaria

- https://es.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search

La búsqueda binaria es un algoritmo eficiente para encontrar un elemento en una lista ordenada de elementos. Funciona al dividir repetidamente a la mitad la porción de la lista que podría contener al elemento, hasta reducir las ubicaciones posibles a solo una.

Veamos cómo describir cuidadosamente la búsqueda binaria. La idea principal de la búsqueda binaria es llevar un registro del rango actual de intentos razonables. Digamos que estoy pensando en un número entre uno y 100, justo como en el juego de adivinar. Si ya intentaste decir 25 y te dije que mi número es más grande, y ya intentaste decir 81 y te dije que mi número es más chico, entonces los números en el rango de 26 a 80 son los únicos intentos razonables.

En cada turno, haces un intento que divide el conjunto de intentos razonables en dos rangos de aproximadamente el mismo tamaño. Si tu intento no es correcto, entonces te digo si es muy alto o muy bajo, y puedes eliminar aproximadamente la mitad de los intentos razonables. Por ejemplo, si el rango actual de los intentos razonables es de 26 a 80, intentarías adivinar a la mitad del camino, (26 + 80) / 2(26+80)/2left parenthesis, 26, plus, 80, right parenthesis, slash, 2, o 53. Si después te digo que 53 es demasiado alto, puedes eliminar todos los números de 53 a 80, dejando 26 a 52 como el nuevo rango de intentos razonables, reduciendo a la mitad el tamaño del rango.


# Step by step

Aquí está una descripción paso a paso de cómo usar la búsqueda binaria para jugar el juego de adivinar:

1. Sea min = 1 y max = n

2. Adivina el promedio de max y min, redondeado hacia abajo de modo que sea un entero

3. Si adivinaste el número, detente. ¡Lo encontraste!

4. Si el intento fue demasiado bajo, haz que min sea uno más grande
que el intento.

5. Si el intento fue demasiado bajo, haz que min sea uno más grande
que el intento.

6. Regresa al paso dos.

Ejemplo en python

```python

# Usando bucle while
def binary_search(array, query):
    lo, hi = 0, len(array) - 1
    while lo <= hi:
        mid = (hi + lo) // 2
        val = array[mid]
        if val == query:
            return mid
        elif val < query:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


# De manera recursiva
def binary_search_recur(array, low, high, val):
    if low > high:       # error case
        return -1
    mid = (low + high) // 2
    if val < array[mid]:
        return binary_search_recur(array, low, mid - 1, val)
    elif val > array[mid]:
        return binary_search_recur(array, mid + 1, high, val)
    else:
        return mid



if __name__ == "__main__":
    arr = [2,5,8,9,10,20,30,40,50,60,70,80]
    index = binary_search_recur(arr,arr[0],len(arr)-1,20)    
    print('el valor esta en el indice {}'.format(index))
```


## Tiempo de ejecución de la búsqueda binaria

Sabemos que una búsqueda lineal en un arreglo de nnn elementos puede tomar hasta nnn intentos.