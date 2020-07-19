def selection_sort(array):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                temporary = array[i]
                array[i] = array[j]
                array[j] = temporary

    return array


print(selection_sort([2, 9, 5, 4, 8, 1, 6]))
print(selection_sort([1, 9, 4.5, 10.6, 5.7, -4.5]))
print(selection_sort([2, 9, 5, 4, 8, 1, 6]))
