class Dict_Table:
    def __init__(self):
        self.max = 100
        self.arr = [[] for i in range(self.max)]

    def get_Dict(self,key):
        d = 0
        for char in key:
            d += ord(char)
        return d % self.max

    def __getitem__(self, key):
        d = self.get_Dict(key)
        for element in self.arr[d]:
            if element[0] == key:
                return print(element[1])


    def __setitem__(self, key, value):
        d = self.get_Dict(key)
        element_found = False
        for ind,element in enumerate(self.arr[d]):
            if len(element) == 2 and element[0] == key:
                self.arr[d][ind] = (key,value)
                element_found = True
                break
        if not element_found:
            self.arr[d].append((key, value))

    def __delitem__(self, key):
        d = self.get_Dict(key)
        for ind,element in enumerate(self.arr[d]):
            if element[0] == key:
                del self.arr[d][ind]

t = Dict_Table()
t.__setitem__("march 6",1)
t.__setitem__("march 17",12)
t.__getitem__("march 17")
t.__getitem__("march 6")
t.__delitem__("march 17")
t.__getitem__("march 17")



