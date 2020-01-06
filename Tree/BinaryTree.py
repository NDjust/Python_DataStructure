class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def size(self):
        ls = self.left.size() if self.left else 0
        rs = self.right.size() if self.right else 0

        return ls + rs + 1

    def depth(self):
        ld = self.left.depth() if self.left else 0
        rd = self.right.depth() if self.right else 0

        return max(ld, rd) + 1

    def inorder(self):
        traversal = []

        if self.left:
            traversal += self.left.inoder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()

        return traversal

    def preorder(self):
        traversal = []

        traversal.append(self.data)

        if self.left:
            traversal += self.left.preorder()

        if self.right:
            traversal += self.right.preorder()

    def postorder(self):
        traversal = []

        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()

        traversal.append(self.data)


class BinaryTree:

    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []

    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []

# make tree method
def make_tree():
    pass


if __name__ == "__main__":
    # add test case
    pass