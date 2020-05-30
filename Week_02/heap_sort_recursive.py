def heapify(arr, heap_size, index):
    """To heapify subtree rooted at index i.
    n is size of heap

    :param arr:
    :param heap_size:
    :param index:
    :return:
    """
    largest = index              # Initialize largest as root
    left_child = 2 * index + 1   # left = 2*i + 1
    right_child = 2 * index + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if left_child < heap_size and arr[index] < arr[left_child]:
        largest = left_child

    # See if right child of root exists and is
    # greater than root
    if right_child < heap_size and arr[largest] < arr[right_child]:
        largest = right_child

    # Change root, if needed
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]  # swap
        # Heapify the root.
        heapify(arr, heap_size, largest)


# The main function to sort an array of given size
def heap_sort(arr):
    size = len(arr)
    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(size // 2 - 1, -1, -1):
        heapify(arr, size, i)
    print(arr)

    # One by one extract elements
    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
n = len(arr)
print("Sorted array is")
print(arr)