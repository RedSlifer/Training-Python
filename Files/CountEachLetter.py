def main():
    file = open('kings.txt', 'r')

    amount_each_letter = 26 * [0]    # Create and initialize amount_each_letter with zeros
    for line in file:
        count_letter(line.lower(), amount_each_letter)

    for i in range(len(amount_each_letter)):
        if amount_each_letter[i] != 0:
            print(f"{chr(ord('a') + i)} appears {amount_each_letter[i]} {'time' if amount_each_letter[i] == 1 else 'times'}")


def count_letter(string, array):
    for character in string:
        if character.isalpha():
            array[ord(character) - ord('a')] += 1


main()
