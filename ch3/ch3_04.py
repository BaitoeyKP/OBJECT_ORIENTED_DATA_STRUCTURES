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


S = Stack()
inp = input('Enter Input : ').split(',')

n = 0
t = []
lt = 0
blt = 0
for i in range(len(inp)):
    if inp[i] != 'B':
        h = inp[i].split(' ')
        for j in range(len(h)):
            if h[j] != 'A':
                lt = h[j]
                t.append(lt)
    elif inp[i] == 'B':
        if len(t) == 0:
            n = 0
        else:
            if inp[i-1] == 'B':
                n = n
            else:
                n = 1
                for k in range(len(t), 0, -1):
                    if int(lt) >= int(t[k-1]):
                        n = n
                    elif int(lt) < int(t[k-1]):
                        n += 1
                        lt = t[k-1]
        S.push(n)
        print(S.pop())
