class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        elif data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)

        elif data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)

    def search(self, value):
        if value == self.data:
            return True

        elif value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False

        elif value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def in_order_traversal(self):
        array = []
        if self.left:
            array += self.left.in_order_traversal()

        array.append(self.data)  # Base root value

        if self.right:
            array += self.right.in_order_traversal()
        return array

    def max(self):
        if self.right is None:
            return self.data
        return self.right.max()

    def min(self):
        if self.left is None:
            return self.data
        return self.left.min()

    def delete_value(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete_value(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete_value(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            minimum = self.right.min()
            self.data = minimum
            self.right = self.right.delete_value(minimum)

        return self


def make_tree(array):
    root = BinaryTreeNode(array[0])
    for i in range(1, len(array)):
        root.add_child(array[i])

    return root


if __name__ == "__main__":
    numbers = [11, 9, 2, 7, 29, 15, 28]
    number_tree = make_tree(numbers)
    print(number_tree.in_order_traversal())
    print(number_tree.search(29))
    print(number_tree.search(100))
    number_tree.delete_value(7)
    print("after delete of 7", number_tree.in_order_traversal())