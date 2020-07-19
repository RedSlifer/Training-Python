import pickle


def main():
    # Open file for writing binary
    file_for_writing = open('numbers.dat', 'wb')

    data = int(input('Enter an integer (the entry exists ' + 'if the entry is different from 0): '))

    while data != 0:
        pickle.dump(data, file_for_writing)
        data = int(input('Enter an integer (the entry exists if the entry is different from 0): '))

    file_for_writing.close()

    # Open file for reading binary
    file_for_reading = open('numbers.dat', 'rb')

    end_of_file = False
    while not end_of_file:
        try:
            print(pickle.load(file_for_reading), end=' ')
        except EOFError:
            end_of_file = True

    file_for_reading.close()

    print('\nAll objects are read')


main()
