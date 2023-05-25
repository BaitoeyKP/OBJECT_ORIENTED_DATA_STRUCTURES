class Node:
    def __init__(self, data, next=None):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if not self.isEmpty():
            p = self.head
            s = ''
            while p != None:
                s += p.data
                s += ' '
                p = p.next
            return s
        else:
            return '0'

    def appendSort(self, data, u):
        p = self.head
        n = Node(data)
        if p is None:
            n.data = data
            self.head = n
            return
        if int(p.data) % (u*10) > int(data) % (u*10):
            n.data = data
            n.next = p
            self.head = n
            return
        while p.next is not None:
            if int(p.next.data) % (u*10) > int(data) % (u*10):
                break
            p = p.next
        n.data = data
        n.next = p.next
        p.next = n
        return

    def size(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count

    def isEmpty(self):
        current_node = self.head
        return current_node == None

    def printList(self):
        p = self.head
        a = ''
        while p != None:
            a += str(p.data)
            if p.next != None:
                a += ' -> '
            p = p.next
        return a

    def str_reverse(self):
        prev = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def clear(self):
        while (self.head != None):
            p = self.head
            self.head = self.head.next
            p = None

    def append(self, data):
        p = Node(data)
        if self.head == None:  # null list
            self.head = p
            return
        t = self.head
        while t.next != None:
            t = t.next
        t.next = p


def radixSort(arr):
    a0, a1, a2, a3, a4 = LinkedList(), LinkedList(
    ), LinkedList(), LinkedList(), LinkedList()
    a5, a6, a7, a8, a9 = LinkedList(), LinkedList(
    ), LinkedList(), LinkedList(), LinkedList()
    an0, an1, an2, an3, an4 = LinkedList(), LinkedList(
    ), LinkedList(), LinkedList(), LinkedList()
    an5, an6, an7, an8, an9 = LinkedList(), LinkedList(
    ), LinkedList(), LinkedList(), LinkedList()
    a00 = LinkedList()
    r = 0
    u = 1
    while r < len(maxV):
        print('------------------------------------------------------------')
        print('Round :', r+1)
        a0.clear()
        a1.clear()
        a2.clear()
        a3.clear()
        a4.clear()
        a5.clear()
        a6.clear()
        a7.clear()
        a8.clear()
        a9.clear()
        an0.clear()
        an1.clear()
        an2.clear()
        an3.clear()
        an4.clear()
        an5.clear()
        an6.clear()
        an7.clear()
        an8.clear()
        an9.clear()
        a00.clear()
        for i in range(len(arr)):
            a = (abs(int(arr[i])) // u) % 10
            if a == 0:
                if int(arr[i]) != 0 or (int(arr[i]) == 0 and int(arr[i-1]) % 10 == 0):
                    if int(arr[i]) >= 0:
                        a0.appendSort(arr[i], u)
                    else:
                        an0.appendSort(arr[i], u)
                else:
                    a00.append(arr[i])
            elif a == 1:
                if int(arr[i]) > 0:
                    a1.appendSort(arr[i], u)
                else:
                    an1.appendSort(arr[i], u)
            elif a == 2:
                if int(arr[i]) > 0:
                    a2.appendSort(arr[i], u)
                else:
                    an2.appendSort(arr[i], u)
            elif a == 3:
                if int(arr[i]) > 0:
                    a3.appendSort(arr[i], u)
                else:
                    an3.appendSort(arr[i], u)
            elif a == 4:
                if int(arr[i]) > 0:
                    a4.appendSort(arr[i], u)
                else:
                    an4.appendSort(arr[i], u)
            elif a == 5:
                if int(arr[i]) > 0:
                    a5.appendSort(arr[i], u)
                else:
                    an5.appendSort(arr[i], u)
            elif a == 6:
                if int(arr[i]) > 0:
                    a6.appendSort(arr[i], u)
                else:
                    an6.appendSort(arr[i], u)
            elif a == 7:
                if int(arr[i]) > 0:
                    a7.appendSort(arr[i], u)
                else:
                    an7.appendSort(arr[i], u)
            elif a == 8:
                if int(arr[i]) > 0:
                    a8.appendSort(arr[i], u)
                else:
                    an8.appendSort(arr[i], u)
            elif a == 9:
                if int(arr[i]) > 0:
                    a9.appendSort(arr[i], u)
                else:
                    an9.appendSort(arr[i], u)
        print('0 : ', end='')
        if not an0.isEmpty():
            print(an0, end='')
        if not a00.isEmpty():
            print(a00, end='')
        if not a0.isEmpty():
            print(a0, end='')
        print()
        print('1 : ', end='')
        if not an1.isEmpty():
            print(an1, end='')
        if not a1.isEmpty():
            print(a1, end='')
        print()
        print('2 : ', end='')
        if not an2.isEmpty():
            print(an2, end='')
        if not a2.isEmpty():
            print(a2, end='')
        print()
        print('3 : ', end='')
        if not an3.isEmpty():
            print(an3, end='')
        if not a3.isEmpty():
            print(a3, end='')
        print()
        print('4 : ', end='')
        if not an4.isEmpty():
            print(an4, end='')
        if not a4.isEmpty():
            print(a4, end='')
        print()
        print('5 : ', end='')
        if not an5.isEmpty():
            print(an5, end='')
        if not a5.isEmpty():
            print(a5, end='')
        print()
        print('6 : ', end='')
        if not an6.isEmpty():
            print(an6, end='')
        if not a6.isEmpty():
            print(a6, end='')
        print()
        print('7 : ', end='')
        if not an7.isEmpty():
            print(an7, end='')
        if not a7.isEmpty():
            print(a7, end='')
        print()
        print('8 : ', end='')
        if not an8.isEmpty():
            print(an8, end='')
        if not a8.isEmpty():
            print(a8, end='')
        print()
        print('9 : ', end='')
        if not an9.isEmpty():
            print(an9, end='')
        if not a9.isEmpty():
            print(a9, end='')
        print()
        u *= 10
        r += 1
    cn0 = an0.printList()
    c00 = a00.printList()
    cn1 = an1.printList()
    cn2 = an2.printList()
    cn3 = an3.printList()
    cn4 = an4.printList()
    cn5 = an5.printList()
    cn6 = an6.printList()
    cn7 = an7.printList()
    cn8 = an8.printList()
    cn9 = an9.printList()
    c0 = a0.printList()
    c1 = a1.printList()
    c2 = a2.printList()
    c3 = a3.printList()
    c4 = a4.printList()
    c5 = a5.printList()
    c6 = a6.printList()
    c7 = a7.printList()
    c8 = a8.printList()
    c9 = a9.printList()
    if not an9.isEmpty():
        after.append(cn9)
    if not an8.isEmpty():
        after.append(cn8)
    if not an7.isEmpty():
        after.append(cn7)
    if not an6.isEmpty():
        after.append(cn6)
    if not an5.isEmpty():
        after.append(cn5)
    if not an4.isEmpty():
        after.append(cn4)
    if not an3.isEmpty():
        after.append(cn3)
    if not an2.isEmpty():
        after.append(cn2)
    if not an1.isEmpty():
        after.append(cn1)
    if not an0.isEmpty():
        after.append(cn0)
    if not a00.isEmpty():
        after.append(c00)
    if not a0.isEmpty():
        after.append(c0)
    if not a1.isEmpty():
        after.append(c1)
    if not a2.isEmpty():
        after.append(c2)
    if not a3.isEmpty():
        after.append(c3)
    if not a4.isEmpty():
        after.append(c4)
    if not a5.isEmpty():
        after.append(c5)
    if not a6.isEmpty():
        after.append(c6)
    if not a7.isEmpty():
        after.append(c7)
    if not a8.isEmpty():
        after.append(c8)
    if not a9.isEmpty():
        after.append(c9)


def maxValue(arr):
    a = 0
    for i in range(len(arr)):
        if abs(int(arr[i])) > abs(int(a)):
            a = arr[i]
        else:
            continue
    return str(abs(int(a)))


inp = input('Enter Input : ').split()
before = LinkedList()
after = LinkedList()
d = 0
c = inp[0]
for i in range(len(inp)):
    before.append(inp[i])
    if inp[i] == c:
        d = 1
        c = inp[i]
    else:
        d = 0
if d == 0:
    maxV = maxValue(inp)
    radixSort(inp)
    print('------------------------------------------------------------')
    print(len(maxV), end='')
    print(' Time(s)')
    print('Before Radix Sort : ', end='')
    print(before.printList())
    print('After  Radix Sort : ', end='')
    print(after.printList())
else:
    print('------------------------------------------------------------')
    print('0 Time(s)')
    print('Before Radix Sort : ', end='')
    print(before.printList())
    print('After  Radix Sort : ', end='')
    print(before.printList())
