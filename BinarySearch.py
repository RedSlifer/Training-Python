def binary_search(array, target):
    start_index = 0
    final_index = len(array) - 1

    while start_index <= final_index:
        middle_index = (start_index + final_index) // 2
        if target == array[middle_index]:
            return middle_index
        elif target > array[middle_index]:
            start_index = middle_index + 1
        elif target < array[middle_index]:
            final_index = middle_index - 1

    return 'Target not found'


print(binary_search([2, 4, 7, 10, 11, 45, 50, 59, 60, 66, 69, 70, 79], 0))
