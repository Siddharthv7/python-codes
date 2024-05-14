def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [x for x in array[1:] if x <= pivot]
        great = [x for x in array[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(great)

array = [3, 14, 9, 10, 6, 11]
sorted_array = quick_sort(array)
print("Original array:", array)
print("Sorted array:", sorted_array)
