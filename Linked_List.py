class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_begning(self, data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            return print("linked list is empty")
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head  = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr=itr.next
        itr.next = Node(data ,None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana", "orange", "pineapple", "grapes"])
    ll.insert_at_begning(5)
    ll.insert_at_begning(89)
    ll.insert_at_end(58)
    ll.insert_at_end(65)
    ll.print()


