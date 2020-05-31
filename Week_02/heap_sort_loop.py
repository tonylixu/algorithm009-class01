def max_child(arr, i, size):
    """For a given node i, return its min child"""
    # Check if the given node has two children
    if i * 2 + 2 >= size:
        return i * 2 + 1
    else:
        if arr[i * 2 + 1] > arr[i * 2 + 2]:
            return i * 2 + 1
        else:
            return i * 2 + 2


def heapifydown(arr, i, size):
    """We need to check all the children of position i, before we can determine where to
    put it at the right place
    """
    while i * 2 + 2 <= size:
        max_c = max_child(arr, i, size)
        if arr[i] < arr[max_c]:
            arr[i], arr[max_c] = arr[max_c], arr[i]
        i = max_c
    return arr


def build_binary_heap(arr):
    """To build from a list, we start from the middle"""
    i = len(arr) // 2
    size = len(arr)
    while i >= 0:
        heapifydown(arr, i, size)
        i -= 1
    return arr


def heap_sort(arr):
    build_binary_heap(arr)
    size = len(arr)
    result = []
    for i in range(size-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        result.append(arr[i])
        arr.pop()
        build_binary_heap(arr)
    result.append(arr[-1])
    print(list(reversed(result)))

s = [12, 11, 13, 5, 6, 7]
heap_sort(s)