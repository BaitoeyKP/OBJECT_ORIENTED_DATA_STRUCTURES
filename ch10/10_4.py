class hash:
    def __init__(self, maxSize, maxCollision, Threshold):
        self.table = []
        for i in range(maxSize):
            self.table.append(None)
        self.maxSize = maxSize
        self.maxCollision = maxCollision
        self.Threshold = Threshold

    def insert(self, value):
        index = 0
        if not self.isFull():
            index = value % self.maxSize
            if self.table[index] == None:
                self.table[index] = value
            elif self.table[index] != None:
                r = 0
                newIndex = index
                print('collision number {0} at {1}'.format(r + 1, newIndex))
                while self.table[newIndex] != None:
                    r += 1
                    newIndex = (index + (r**2)) % self.maxSize
                    if (self.maxCollision <= r):
                        print('****** Max collision - Rehash !!! ******')
                        return False
                    if self.table[newIndex] == None:
                        self.table[newIndex] = value
                        break
                    print('collision number {0} at {1}'.format(
                        r + 1, newIndex))
            return True
        else:
            print('****** Data over threshold - Rehash !!! ******')
            return False

    def isFull(self):
        k = int(self.maxSize * self.Threshold / 100)
        l = 0
        for i in self.table:
            if i != None:
                l += 1
        if l >= k:
            return True
        return False

    def print(self):
        for i in range(len(self.table)):
            print('#{0}'.format(i + 1), end='')
            print(' ' * (7-len(str(i + 1))), end='')
            print('{0}'.format(self.table[i]))


def findClosest(value):
    while True:
        value += 1
        for i in range(2, value):
            if value % i == 0:
                break
            if i == value - 1:
                return value


print(' ***** Rehashing *****')
inp = input('Enter Input : ').split('/')
inp1 = inp[0]
inp2 = inp[1]
sizeTable, maxCollision, Threshold = map(int, inp1.split())
data = []
for e in inp2.split():
    data.append(int(e))
print('Initial Table :')
hashTable = hash(sizeTable, maxCollision, Threshold)
hashTable.print()
print('----------------------------------------')
hashTable.isFull()
lastAdd = -1
notAlldata = True
while notAlldata:
    for i in range(len(data)):
        if i >= lastAdd + 1:
            print('Add : ' + str(data[i]))
        if not hashTable.insert(data[i]):
            hashTable = hash(findClosest(hashTable.maxSize * 2),
                             maxCollision, Threshold)
            lastAdd = i
            break
        else:
            if i >= lastAdd:
                hashTable.print()
                print('----------------------------------------')
        if i == len(data) - 1:
            notAlldata = False
