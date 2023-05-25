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

    def _insert(root, data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = BST._insert(root.left, data)
            else:
                root.right = BST._insert(root.right, data)
        return root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def printTree3(self, node, k, level=0):
        if node != None:
            self.printTree3(node.right, k, level + 1)
            if int(str(node)) > k:
                print('     ' * level, int(str(node)) * 3)
            else:
                print('     ' * level, node)
            self.printTree3(node.left, k, level + 1)


T = BST()
inp = input('Enter Input : ').split('/')
inpl = inp[0].split()
k = int(inp[1])
for i in range(len(inpl)):
    root = T.insert(int(inpl[i]))
T.printTree(root)
print('--------------------------------------------------')
T.printTree3(root, k)
