def main():
    # Open file
    file = open('kings.txt', 'r')

    # Read all data from the file
    print(file.read())
    file.close()

    file = open('kings.txt', 'r')
    string_1 = file.read(6)   # Read characters
    print(string_1)
    string_2 = file.read(13)
    print(repr(string_2))
    file.close()

    print()

    file = open('kings.txt', 'r')
    line_1 = file.readline()
    line_2 = file.readline()
    line_3 = file.readline()
    print(repr(line_1))
    print(repr(line_2))
    print(repr(line_3))
    file.close()

    print()

    file = open('kings.txt', 'r')
    print(file.readlines())
    file.close()


main()
