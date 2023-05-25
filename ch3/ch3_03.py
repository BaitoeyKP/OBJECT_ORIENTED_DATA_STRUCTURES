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


def postFixeval(st):
    s = Stack()
    ans = ''
    for i in range(len(st)):
        if st[i] != '+' and st[i] != '-' and st[i] != '*' and st[i] != '/':
            s.push(st[i])
        # elif st[i] == '+' or st[i] == '-' or st[i] == '*' or st[i] != '/':
        else:
            r = s.pop()
            l = s.pop()
            if st[i] == '+':
                ans = float(l) + float(r)
            elif st[i] == '-':
                ans = float(l) - float(r)
            elif st[i] == '*':
                ans = float(l) * float(r)
            elif st[i] == '/':
                ans = float(l) / float(r)
            s.push(ans)
    return s.pop()


print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split(' '))
print("Answer : ", '{:.2f}'.format(postFixeval(token)))
