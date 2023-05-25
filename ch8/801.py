class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right

    def __str__(self):
        return str(self.data)

    def getData(self):  # accessor
        return self.data

    def getLeft(self):  # accessor
        return self.left

    def getRight(self):  # accessor
        return self.right

    def setData(self, data):  # mutator
        self.data = data

    def setLeft(self, left):  # mutator
        self.left = left

    def setRight(self, right):  # mutator
        self.right = right


class BST:
    def __init__(self, root=None):
        self.root = None if root is None else root

    def insert(self, data):
        self.root = BST._insert(self.root, data)
        return self.root

    def _insert(root, data, ans=''):
        if root is None:
            print(ans, end='')
            print('*')
            return Node(data)
        else:
            if data < root.data:
                root.left = BST._insert(root.left, data, ans=ans + 'L')
            else:
                root.right = BST._insert(root.right, data, ans=ans + 'R')
        return root


tree = BST()
inp = input('Enter Input : ').split()
for i in range(len(inp)):
    root = tree.insert(int(inp[i]))
