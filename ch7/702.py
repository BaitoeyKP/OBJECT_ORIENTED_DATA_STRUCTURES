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


def minT(root):
    if root is None:
        return float('inf')
    min = root.data
    lmin = minT(root.left)
    rmin = minT(root.right)
    if lmin < min:
        min = lmin
    if rmin < min:
        min = rmin
    return min


def maxT(root):
    if root is None:
        return float('-inf')
    max = root.data
    lmax = maxT(root.left)
    rmax = maxT(root.right)
    if lmax > max:
        max = lmax
    if rmax > max:
        max = rmax
    return max


T = BST()
inp = input('Enter Input : ').split()
for i in range(len(inp)):
    root = T.insert(int(inp[i]))
T.printTree(root)
print('--------------------------------------------------')
print('Min : ', end='')
print(minT(root))
print('Max : ', end='')
print(maxT(root))
