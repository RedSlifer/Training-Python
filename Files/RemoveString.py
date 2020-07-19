import os


def main():
    word = str(input('Enter the word to remove from file: '))
    origin_file = open('kings.txt', 'r')
    target_file = open('kings_1.txt', 'w')

    for line in origin_file:
        target_file.write(line.replace(word, ''))

    origin_file.close()
    target_file.close()

    os.remove('kings.txt')
    os.rename('kings_1.txt', 'kings.txt')


main()
