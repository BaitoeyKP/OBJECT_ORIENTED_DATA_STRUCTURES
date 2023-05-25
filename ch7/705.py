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


class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        return str(self.items)

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def isOperator(c):
    return c == '+' or c == '-' or c == '*' or c == '/' or c == '^'


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end='')


def inorder(root):
    if root is None:
        return
    if isOperator(root.data):
        print('(', end='')
    inorder(root.left)
    print(root.data, end='')
    inorder(root.right)
    if isOperator(root.data):
        print(')', end='')


def preorder(root):
    if root is None:
        return
    print(root.data, end='')
    preorder(root.left)
    preorder(root.right)


def construct(postfix):
    if not postfix:
        return
    s = Stack()
    for c in postfix:
        if isOperator(c):
            x = s.pop()
            y = s.pop()
            node = Node(c, y, x)
            s.push(node)
        else:
            s.push(Node(c))
    return s.peek()


def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)


inp = input('Enter Postfix : ')
root = construct(inp)
print('Tree : ')
printTree(root)
print('--------------------------------------------------')
print('Infix : ', end='')
inorder(root)
print('\nPrefix : ', end='')
preorder(root)
