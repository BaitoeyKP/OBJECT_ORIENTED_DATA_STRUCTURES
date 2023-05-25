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


x = input('Enter Input : ').split(',')
q = Queue()
numArray = []
for i in range(len(x)):
    if x[i] != 'D':
        num = x[i].split(' ')
        for j in range(len(num)):
            if num[j] != 'E':
                numArray.append(num[j])
                q.enQueue(num[j])
                print(q.size())
    elif x[i] == 'D':
        if q.isEmpty() == 1:
            print('-1')
        else:
            print(q.deQueue(), '0')
if q.isEmpty() == 1:
    print('Empty')
else:
    for k in range(q.size()):
        print(q.deQueue(), end=' ')
