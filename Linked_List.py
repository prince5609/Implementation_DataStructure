class Node:
    def __init__(self, data=None, next=None):
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
            return
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
    length = b.get_length()
    if a.get_data(0) >= b.get_data(0):
        a.insert_at(0, b.get_data(0))
        j = 1
        i = 1
    else:
        j = 0
        i = 1
    while j < length:
        if a.get_data(i) >= b.get_data(j):
            a.insert_at(i, b.get_data(j))
            j += 1
        i += 1
    while j < length:
        a.insert_at(i, b.get_data(j))
        j += 1
        i += 1
    return a.print()


def mergeTwoLists_by_nodes(l1, l2):
    dummy_node = Node(0, None)
    tail = dummy_node
    while True:
        if l1 is None:
            tail.next = l2
            break
        if l2 is None:
            tail.next = l1
            break
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    return dummy_node.next


if __name__ == "__main__":
    obj1 = Linked_list()
    obj1.insert_at_beginning(1)
    obj1.insert_at_end(3)
    obj1.insert_at_end(5)
    obj1.insert_at_end(8)
    obj1.insert_at_end(9)
    obj1.insert_at_end(12)
    obj1.insert_at_end(20)
    obj1.print()
    obj1.remove_at(4)
    obj1.print()
    obj1.insert_at(3, 18)
    obj1.print()
    print("Length of list1 = " + str(obj1.get_length()))
    print("data at index 2 in List1 = " + str(obj1.get_data(2)))

    obj2 = Linked_list()
    obj2.insert_at_end(1)
    obj2.insert_at_end(2)
    obj2.insert_at_end(3)
    obj2.insert_at_end(4)
    obj2.insert_at_end(5)
    obj2.print()

    merge_two_linked_list(obj1, obj2)
    mergeTwoLists_by_nodes(obj1.head, obj2.head)
