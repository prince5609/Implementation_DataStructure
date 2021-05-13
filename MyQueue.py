from collections import deque
class MyQueue:
    def __init__(self):
        self.a = deque()

    def pop(self):
        return self.a.pop()

    def push(self,val):
        return (self.a.appendleft(val))

    def is_empty(self):
        return len(self.a) == 0

    def size(self):
        return len(self.a)

obj = MyQueue()
obj.push(3)
obj.push(4)
obj.push(5)
obj.push(8)
obj.pop()
print(obj.a)


