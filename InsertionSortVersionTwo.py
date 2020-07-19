def insertion_sort(array):
    for i in range(1, len(array)):
        pivot = array[i]
        counter = i - 1

        while counter >= 0 and array[counter] > pivot:
            array[counter + 1] = array[counter]
            counter -= 1

        array[counter + 1] = pivot

    return array


print(insertion_sort([2, 2, 2, 9, 5, 4, 8, 1, 2, 6]))
