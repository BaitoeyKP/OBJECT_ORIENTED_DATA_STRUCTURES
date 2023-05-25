class node:
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

    def add(self, data):
        self.root = BST._add(self.root, data)

    def _add(root, data):
        if root is None:
            return node(data)
        else:
            if data < root.data:
                root.left = BST._add(root.left, data)
            else:
                root.right = BST._add(root.right, data)
        return root

    def inOrder(self):
        BST._inOrder(self.root)

    def _inOrder(root):
        if root is not None:
            BST._inOrder(root.getLeft())
            print(root, end=' ')
            BST._inOrder(root.getRight())

    def preOrder(self):
        BST._preOrder(self.root)

    def _preOrder(root):
        if root is not None:
            print(root, end=' ')
            BST._preOrder(root.getLeft())
            BST._preOrder(root.getRight())

    def postOrder(self):
        BST._postOrder(self.root)

    def _postOrder(root):
        if root is not None:
            BST._postOrder(root.getLeft())
            BST._postOrder(root.getRight())
            print(root, end=' ')

    def leverOrder(self):
        q = Queue()
        q.enQ(self.root)
        while q.isEmpty() is not True:
            n = q.deQ()
            print(n.getData(), end=' ')
            if n.getLeft() is not None:
                q.enQ(n.getLeft())
            if n.getRight() is not None:
                q.enQ(n.getRight())


class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQ(self, i):
        self.items.append(i)  # insert i ที;ท้าย list

    def deQ(self):
        return self.items.pop(0)  # pop out index 0

    def isEmpty(self):
        return self.items == []


inp = input('Enter Input : ').split()
tree = BST()
for i in range(len(inp)):
    tree.add(int(inp[i]))
print('Preorder : ', end='')
tree.preOrder()
print('\nInorder : ', end='')
tree.inOrder()
print('\nPostorder : ', end='')
tree.postOrder()
print('\nBreadth : ', end='')
tree.leverOrder()
