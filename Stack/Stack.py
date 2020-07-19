class Stack:
    def __init__(self):
        self.__elements = list()

    def is_empty(self):
        return len(self.__elements) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.__elements[len(self.__elements) - 1]

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.__elements.pop()

    def get_size(self):
        return len(self.__elements)
