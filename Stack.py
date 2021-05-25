from collections import deque


class stack:
    def __init__(self):
        self.a = deque()

    def pop(self):
        return self.a.pop()

    def push(self, val):
        return self.a.append(val)

    def peek(self):
        return self.a[-1]

    def is_empty(self):
        return len(self.a) == 0

    def size(self):
        return len(self.a)


obj = stack()
obj.push(3)
obj.push(4)
obj.push(5)
obj.push(8)
obj.pop()
print(obj.a)
