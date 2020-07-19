def main():
    hexadecimal_number = input('Enter a hexadecimal number: ').strip()

    decimal_number = hexadecimal_to_decimal(hexadecimal_number.upper())

    if decimal_number is None:
        print('Incorrect hexadecimal number')
    else:
        print(f'The decimal value for hexadecimal number {hexadecimal_number} is {decimal_number}')


def hexadecimal_to_decimal(hexadecimal_number):
    decimal_number = 0

    for i in range(len(hexadecimal_number)):
        hexadecimal_character = hexadecimal_number[i]

        if 'A' <= hexadecimal_character <= 'F' or '0' <= hexadecimal_character <= '9':
            decimal_number = decimal_number * 16 + hexadecimal_char_to_decimal(hexadecimal_character)
        else:
            return None

    return decimal_number


def hexadecimal_char_to_decimal(hexadecimal_character):
    if 'A' <= hexadecimal_character <= 'F':
        return 10 + ord(hexadecimal_character) - ord('A')
    else:
        return ord(hexadecimal_character) - ord('0')


main()
