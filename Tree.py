class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        n = self.parent
        while n:
            level += 1
            n = n.parent
        return level

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print(self):
        spaces = " " * self.get_level() * 3
        symbol = spaces + "--->" if self.parent else ""
        print(symbol + self.data)
        if self.children:
            for child in self.children:
                child.print()


def make_tree():
    root = TreeNode("World")

    Country1 = TreeNode("India")
    city = TreeNode("Delhi")
    city.add_child(TreeNode("Dark"))
    Country1.add_child(city)
    Country1.add_child(TreeNode("Maharashtra"))
    Country1.add_child(TreeNode("Rajasthan"))

    Country2 = TreeNode("America")
    Country2.add_child(TreeNode("Washington D.C"))
    Country2.add_child(TreeNode("California"))
    Country2.add_child(TreeNode("New york"))

    Country3 = TreeNode("Russia")
    Country3.add_child(TreeNode("Altai"))
    Country3.add_child(TreeNode("Brat"))
    Country3.add_child(TreeNode("Sakha"))

    root.add_child(Country1)
    root.add_child(Country2)
    root.add_child(Country3)

    root.print()


if __name__ == '__main__':
    make_tree()
