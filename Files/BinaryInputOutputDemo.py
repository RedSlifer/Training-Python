import pickle


def main():
    # Open file for writing binary
    file_for_writing = open('pickle.dat', 'wb')

    pickle.dump(45, file_for_writing)
    pickle.dump(56.6, file_for_writing)
    pickle.dump('Programming is fun', file_for_writing)
    pickle.dump([1, 2, 3, 4], file_for_writing)
    file_for_writing.close()

    # Open file for reading binary
    file_for_reading = open('pickle.dat', 'rb')

    print(pickle.load(file_for_reading))
    print(pickle.load(file_for_reading))
    print(pickle.load(file_for_reading))
    print(pickle.load(file_for_reading))
    file_for_reading.close()


main()
