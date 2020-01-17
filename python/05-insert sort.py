def insertion_sort(arr, simulation=False):
    """ Insertion Sort
        Complexity: O(n^2)
    """
    
    iteration = 0
    if simulation:
        print("iteration",iteration,":",*arr)
        
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        
        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor
        
        if simulation:
                iteration = iteration + 1
                print("iteration",iteration,":",*arr)

    return arr

if __name__ == "__main__":
    arr = [22, 11, 99, 88, 9, 7, 42]
    insertion_sort(arr,True)