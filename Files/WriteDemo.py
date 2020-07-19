import os.path


def main():
    # Tests if file exists
    if os.path.isfile('kings.txt'):
        print('The file kings.txt already exists')
    else:
        # Open file
        file = open('kings.txt', 'w')

        # Write data to the file
        file.write('Philip II of Spain\n')
        file.write('Henry VII of England\n')
        file.write('Francis I of France\n')

        # Close the file
        file.close()


main()
