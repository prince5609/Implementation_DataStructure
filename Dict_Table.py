class Dict_Table:
    def __init__(self):
        self.max = 10
        self.arr = [None for i in range(self.max)]

    def get_dict(self, key):
        d = 0
        for char in key:
            d += ord(char)
        return d % self.max

    def __setitem__(self, key, val):
        d = self.get_dict(key)
        self.arr[d] = val

    def __getitem__(self, key):  # only get can be use in place of __getitem__
        d = self.get_dict(key)
        return print(self.arr[d])

    def __delitem__(self, key):
        d = self.get_dict(key)
        self.arr[d] = None

    def print(self):
        return print(self.arr)


t = Dict_Table()
t.__setitem__("Name", "Prince")
t.print()
t.__setitem__("Age", 25)
t.print()
t.__setitem__("Gender", "Male")
t.print()
t.__getitem__("Name")
t.__getitem__("Age")
t.__delitem__("Gender")
t.print()
