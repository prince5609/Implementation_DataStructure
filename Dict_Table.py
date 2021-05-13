class Dict_Table:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def get_dict(self,key):
        d = 0
        for char in key:
            d += ord(char)
        return d % self.max

    def __setitem__(self, key,val):
        d = self.get_dict(key)
        self.arr[d] = val

    def __getitem__(self, key):                   # only get can be use in place of __getitem__
        d = self.get_dict(key)
        return print(self.arr[d])

    def __delitem__(self, key):
        d = self.get_dict(key)
        self.arr[d] = None

t = Dict_Table()
t.__setitem__("prince",18)
t.__setitem__("tyagi",20)
t.__getitem__("prince")
t.__getitem__("tyagi")
t.__delitem__("prince")
t.__getitem__("prince")