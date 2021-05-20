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

    India = TreeNode("India")
    India.add_child(TreeNode("Delhi"))
    India.add_child(TreeNode("Maharashtra"))
    India.add_child(TreeNode("Rajasthan"))

    America = TreeNode("America")
    America.add_child(TreeNode("Washington D.C"))
    America.add_child(TreeNode("California"))
    America.add_child(TreeNode("New york"))

    Russia = TreeNode("Russia")
    Russia.add_child(TreeNode("Altai"))
    Russia.add_child(TreeNode("Brat"))
    Russia.add_child(TreeNode("Sakha"))

    root.add_child(India)
    root.add_child(America)
    root.add_child(Russia)

    root.print()


if __name__ == '__main__':
    make_tree()