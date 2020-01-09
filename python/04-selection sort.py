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