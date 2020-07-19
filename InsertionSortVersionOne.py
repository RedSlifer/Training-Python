def insertion_sort(array):
    sorted_array = [array[0]]

    if array[1] >= sorted_array[0]:
        sorted_array.append(array[0])
    else:
        sorted_array.insert(0, array[1])

    for i in range(1, len(array)):
        for j in range(len(sorted_array)):
            if j != len(sorted_array) - 1:
                if array[i] >= sorted_array[j]:
                    continue
                else:
                    sorted_array.insert(j, array[i])
                    break
            else:
                if array[i] >= sorted_array[j]:
                    sorted_array.append(array[i])
                    break
                else:
                    sorted_array.insert(j, array[i])
                    break

    return sorted_array


print(insertion_sort([2, 2, 2, 9, 5, 4, 8, 1, 2, 6]))
