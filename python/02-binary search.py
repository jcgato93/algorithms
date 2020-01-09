
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
    result = binary_search_recur(arr,arr[0],len(arr)-1,20)
    print('el valor esta en el indice {}'.format(result))