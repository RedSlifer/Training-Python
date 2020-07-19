rows = 6
columns = 7


def consecutive_four(matrix):
    # Check rows
    for i in range(rows):
        if next_is_equal(matrix[i], rows):
            return True

    # Check columns
    for j in range(columns):
        column = list()

        for i in range(rows):
            column.append(matrix[i][j])

        if next_is_equal(column, rows):
            return True

    # Check main diagonal (lower triangular matrix)
    for i in range(rows - 3):
        number_elements_diagonal = rows - i
        diagonal = list()

        for k in range(number_elements_diagonal):
            diagonal.append(matrix[k + i][k])

        if next_is_equal(diagonal, number_elements_diagonal):
            return True

    # Check main diagonal (upper triangular matrix)
    for j in range(1, columns - 3):
        number_elements_diagonal = columns - j
        diagonal = list()

        for k in range(number_elements_diagonal):
            diagonal.append(matrix[k][k + j])

        if next_is_equal(diagonal, number_elements_diagonal):
            return True

    # Check anti-diagonal (upper triangular matrix)
    for j in range(3, columns):
        number_elements_diagonal = min(j + 1, rows)
        diagonal = list()

        for k in range(number_elements_diagonal):
            diagonal.append(matrix[k][j - k])

        if next_is_equal(diagonal, number_elements_diagonal):
            return True

    # Check anti-diagonal (lower triangular matrix)
    for i in range(1, rows - 3):
        number_elements_diagonal = rows - i
        diagonal = list()

        for k in range(number_elements_diagonal):
            diagonal.append(matrix[k + i][columns - k - 1])

        if next_is_equal(diagonal, number_elements_diagonal):
            return True

    return False


def next_is_equal(array, length):
    for i in range(length - 3):
        is_equal = True

        for j in range(i, i + 3):
            if array[j] != array[j + 1]:
                is_equal = False
                break

        if is_equal:
            return True

    return False


print(consecutive_four([[0, 1, 0, 3, 1, 6, 1],
                        [0, 1, 6, 8, 6, 0, 1],
                        [5, 6, 2, 1, 8, 2, 9],
                        [6, 5, 1, 6, 1, 9, 1],
                        [1, 1, 3, 1, 4, 0, 7],
                        [3, 3, 3, 3, 4, 0, 7]]))

print(consecutive_four([[0, 1, 0, 3, 1, 6, 1],
                        [0, 1, 6, 8, 6, 1, 1],
                        [5, 6, 2, 1, 0, 2, 9],
                        [6, 5, 1, 1, 1, 9, 1],
                        [1, 1, 3, 1, 4, 0, 7],
                        [3, 3, 3, 2, 4, 0, 7]]))
