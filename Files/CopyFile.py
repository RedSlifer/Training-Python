import os.path
import sys


def main():
    # Check if target file exists
    if os.path.isfile('kings_1.txt'):
        print('kings_1.txt already exists')
        sys.exit()

    # Open files for input and output
    origin = open('kings.txt', 'r')
    target = open('kings_1.txt', 'w')

    for line in origin:
        target.write(line)


main()
