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

    def print(self):
        if self.head is None:
            print("Linked List Is Empty")
        itr = self.head
        link_list = ""
        while itr:
            link_list += str(itr.data) + "-->"
            itr = itr.next
        print(link_list)


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
