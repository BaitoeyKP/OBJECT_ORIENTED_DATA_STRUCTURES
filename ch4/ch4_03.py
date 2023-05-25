class Queue:
    """ class Queue
    default : empty Queue/
    Queue([list])
    """

    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, i):
        self.items.append(i)  # insert i ที;ท้าย list

    def deQueue(self):
        return self.items.pop(0)  # pop out index 0

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


x = input('Enter Input : ').split('/')
q = Queue()
ans = []
d = 0
st = 0
y = x[0].split(' ')
for i in range(len(y)):
    q.enQueue(y[i])
if len(x) == 2:
    a = x[1].split(',')
    for k in range(len(a)):
        if a[k] != 'D':
            b = a[k].split(' ')
            for l in range(len(b)):
                if b[l] != 'E' and b[l] != '':
                    q.enQueue(b[l])
        else:
            if q.isEmpty() == 0:
                q.deQueue()
for m in range(q.size()):
    ans.append(q.deQueue())
# print(ans)
for n in range(len(ans)):
    for o in range(len(ans)):
        if o != n and int(ans[n]) == int(ans[o]):
            d = 1
            st = 1
            break
        else:
            d = 0
    if st == 1:
        break
if d == 1:
    print('Duplicate')
else:
    print('NO Duplicate')
