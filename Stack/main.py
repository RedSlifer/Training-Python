from Stack import Stack

stack = Stack()

for i in range(10):
    stack.push(i)

print(stack.peek())

while not stack.is_empty():
    print(stack.pop(), end=' ')
