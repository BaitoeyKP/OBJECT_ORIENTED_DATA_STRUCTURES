class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return str(self.data)


class AVL(object):
    def __init__(self):
        self.root = None

    def insert(self, node, data):
        if self.root is None:
            self.root = TreeNode(data)
            return self.root
        else:
            if node != None:
                if data <= node.data:
                    node.left = self.insert(node.left, data)
                else:
                    node.right = self.insert(node.right, data)
            else:
                return TreeNode(data)
            l = node.left.height if node.left is not None else -1
            r = node.right.height if node.right is not None else -1
            if abs(l - r) > 1:
                a = self.root
                if l > r:
                    if data <= node.left.data:
                        a = leftLeftRotate(node)
                    else:
                        node.left = rightRightRotate(node.left)
                        node = leftLeftRotate(node)
                        a = node
                else:
                    if data <= node.right.data:
                        node.right = leftLeftRotate(node.right)
                        node = rightRightRotate(node)
                        a = node
                    else:
                        a = rightRightRotate(node)
                changeHeight(a)
                return a
            else:
                node.height = max(l, r) + 1
                return node


def rightRightRotate(px):
    py = px.right
    px.right = py.left
    py.left = px
    return py


def leftLeftRotate(px):
    py = px.left
    px.left = py.right
    py.right = px
    return py


def changeHeight(a):
    if a != None:
        a.height = max(changeHeight(a.left), changeHeight(a.right)) + 1
        return a.height
    else:
        return -1


def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)


def fillData(node, data, k, count=1, q=[]):
    if count > int(k / 2):
        node.data = data.pop(0)
    if node.left:
        q.append(node.left)
    if node.right:
        q.append(node.right)
    if len(q) > 0:
        fillData(q.pop(0), data, k, count + 1, q)


def cutting(node):
    if node.left != None and node.right != None:
        cutting(node.left)
        cutting(node.right)
        node.data = min(node.left.data, node.right.data)
        node.left.data -= node.data
        node.right.data -= node.data


def sumTree(node):
    if node != None:
        return node.data + sumTree(node.left) + sumTree(node.right)
    return 0


myTree = AVL()
root = None
k, data = input('Enter Input : ').split('/')
k = int(k)
data = [int(i)for i in data.split()]
if int(k / 2) + 1 != len(data) or int(k / 2) == k / 2 or k < 3:
    print('Incorrect Input')
else:
    for e in range(k):
        root = myTree.insert(root, 0)
    fillData(root, data, k)
    cutting(root)
    print(sumTree(root))
