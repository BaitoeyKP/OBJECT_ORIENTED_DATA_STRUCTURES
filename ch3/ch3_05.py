class Stack:
    """ class Stack
    default : empty stack / Stack([...])
    """

    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        s = 'stack of ' + str(self.size())+' items : '
        for ele in self.items:
            s += str(ele)+' '
        return s

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


def dec2bin(decnum):
    s = Stack()
    ans = ''
    while decnum > 0:
        a = decnum % 2
        decnum //= 2
        s.push(a)
    while s.isEmpty() == 0:
        ans += str(s.pop())
    return ans


print(" ***Decimal to Binary use Stack***")
token = input("Enter decimal number : ")
print("Binary number : ", end='')
print(dec2bin(int(token)))
