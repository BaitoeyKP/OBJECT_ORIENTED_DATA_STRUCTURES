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


x = input('Enter Input : ').split(',')
s = Stack()
y = ''
z = ''
r = []
for i in range(len(x)):
    if x[i] != 'P':
        y = x[i]
        for j in range(len(y)):
            if y[j] != 'A' and y[j] != ' ':
                z += y[j]
                r.append(y[j])
        print('Add =', z, 'and Size =', s.size()+1)
        s.push(z)
        z = ''
    elif x[i] == 'P':
        if s.isEmpty() == 1:
            print('-1')
        else:
            print('Pop =', s.pop(), ('and Index ='), s.size())
            del r[s.size()*2]
            del r[(s.size()*2)-1]
print('Value in Stack = ', end='')
if s.isEmpty() == 1:
    print('Empty', end='')
else:
    for k in range(len(r)):
        print(r[k], end='')
        if k % 2 == 1:
            print(' ', end='')
