from collections import deque


class Stack:

    def __init__(self):
        self.stack = deque()

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def __str__(self):
        return f'{self.stack}'
    #inside the class reverse all possible stack value
    def reverse_string(self):
        # reverse string using stack
        # first just reverse
        letter = deque()
        reversed=''
        for char in self.stack:
            for c in char:
                letter.append(c)
            for _ in range(0, len(letter)):
                reversed+= ' ' + letter.pop()

        print(reversed)


#outside the class
def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()

    return rstr





print(reverse_string("wasup"))
s = Stack()
s.push("I will conquer the earth")
s.push("No i will conquer")
s.reverse_string()
print(s)
