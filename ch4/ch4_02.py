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


inp = input('Enter people and time : ').split(' ')
p = inp[0]
t = inp[1]
core = Queue()
c1 = Queue()
c2 = Queue()
coreL = []
c1L = []
c2L = []
for i in range(len(p)):
    core.enQueue(p[i])
    coreL.append(p[i])
for j in range(int(t)):
    if core.isEmpty() == 0:
        if c1.size() < 5:
            d1 = core.deQueue()
            c1.enQueue(d1)
            c1L.append(d1)
            del coreL[0]
        elif c2.size() < 5:
            d2 = core.deQueue()
            c2.enQueue(d2)
            c2L.append(d2)
            del coreL[0]
    print(j+1, coreL, c1L, c2L)
    if c1.isEmpty() == 0 and (j+1) % 3 == 0:
        c1.deQueue()
        del c1L[0]
    if c2.isEmpty() == 0 and j % 2 == 0:
        c2.deQueue()
        del c2L[0]
