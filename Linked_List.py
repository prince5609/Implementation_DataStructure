class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        length = 0
        itr = self.head
        while itr:
            length += 1
            itr = itr.next
        return length

    def insert_at(self, index, value):
        if 0 > index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(value)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(value, itr.next)
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if 0 > index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def search(self, index):
        if 0 > index > self.get_length():
            raise Exception("Invalid")

        elif index == 0:
            return self.head.data
        count = 1
        itr = self.head.next
        while itr:
            if count == index:
                return itr.data
            count += 1
            itr = itr.next

    def reverse_list(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev
        return self.head

    def print(self):
        if self.head is None:
            print("Linked List Is Empty")
        itr = self.head
        link_list = ""
        while itr:
            link_list += str(itr.data) + "-->"
            itr = itr.next
        print(link_list)

    def get_data(self, index):
        if 0 > index > self.get_length():
            raise Exception("Invalid")
        if index == 0:
            return self.head.data
        else:
            count = 1
            itr = self.head.next
            while itr:
                if count == index:
                    return itr.data
                count += 1
                itr = itr.next


def merge_two_linked_list(a, b):
    l1 = a.get_length()
    l2 = b.get_length()
    if a.get_data(0) >= b.get_data(0):
        a.insert_at(0, b.get_data(0))
        j = 1
        i = 1
    else:
        j = 0
        i = 1
    while i < l1 and j < l2:
        if a.get_data(i) >= b.get_data(j):
            a.insert_at(i, b.get_data(j))
            j += 1
        i += 1
    while j < l2:
        a.insert_at(i, b.get_data(j))
        j += 1
        i += 1
    return a.print()


if __name__ == "__main__":
    obj = Linked_list()
    obj.insert_at_beginning("Prince")
    obj.print()
    obj.insert_at_beginning("Aryan")
    obj.print()
    obj.insert_at_end("Nishant")
    obj.print()
    obj.insert_at(2, "Myra")
    obj.print()
    obj.remove_at(3)
    obj.print()
    print(obj.get_length())
    print(obj.search(2))
    obj.reverse_list()
    obj.print()

    obj2 = Linked_list()
    obj2.insert_at_end("Ram")
    obj2.insert_at_end("Shyam")
    obj2.insert_at_end("Sita")
    obj2.print()
    merge_two_linked_list(obj, obj2)
