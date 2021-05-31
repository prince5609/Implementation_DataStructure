class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Doubly_LinkList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)

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

    def insert_at(self, index, data):
        if 0 > index > self.get_length():
            raise Exception("Invalid input as index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 1
        itr = self.head
        while itr:
            if count == index:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            count += 1
            itr = itr.next

    def remove_at(self, index):
        if 0 > index > self.get_length():
            raise Exception("Invalid input as index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 1
        itr = self.head.next
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            count += 1
            itr = itr.next

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def print_forward(self):
        if self.head is None:
            print("Link List is empty")
            return
        itr = self.head
        link_list = ""
        while itr:
            link_list += str(itr.data) + "-->"
            itr = itr.next
        print(link_list)

    def print_backward(self):
        if self.head is None:
            print("List Is Empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        link_list = ""
        while itr:
            link_list += str(itr.data) + "-->"
            itr = itr.prev
        print("Reverse List :", link_list)

    def get_data(self, index):
        if 0 > index > self.get_length():
            raise Exception("Invalid input as index")

        if index == 0:
            return self.head.data

        count = 1
        itr = self.head.next
        while itr:
            if count == index:
                return itr.data
            count += 1
            itr = itr.next


if __name__ == "__main__":
    obj1 = Doubly_LinkList()
    obj1.insert_at_beginning(2)
    obj1.insert_at_end(3)
    obj1.insert_at_end(4)
    obj1.insert_at_end(5)
    obj1.print_forward()
    obj1.insert_at_beginning(1)
    obj1.print_forward()
    obj1.print_backward()

    obj1.insert_values([10, 20, 30, 40, 50])
    obj1.print_forward()

    print("Data at index 2 :", obj1.get_data(2))
    print("Length of List :", obj1.get_length())
    obj1.insert_at(2, 25)
    obj1.print_forward()
    obj1.remove_at(3)
    obj1.print_forward()
