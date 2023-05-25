class Node:
    def __init__(self, data, next=None):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = next

    def __str__(self):
        return str(self.data)


def createList(data):
    head = Node(data[0])
    for element in data[1:]:
        p = head
        while p.next:
            p = p.next
        p.next = Node(element)
    return head


def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end=' ')
        ptr = ptr.next


def mergeOrderesList(p, q):
    ans = Node(0)
    tail = ans
    while True:
        if p is None:
            tail.next = q
            break
        if q is None:
            tail.next = p
            break
        if int(p.data) <= int(q.data):
            tail.next = p
            p = p.next
        else:
            tail.next = q
            q = q.next
        tail = tail.next
    return ans.next


inp = input('Enter 2 Lists : ').split()
L1 = inp[0].split(',')
LL1 = createList(L1)
L2 = inp[1].split(',')
LL2 = createList(L2)
print('LL1 : ', end='')
printList(LL1)
print('\nLL2 : ', end='')
printList(LL2)
m = mergeOrderesList(LL1, LL2)
print('\nMerge Result : ', end='')
printList(m)
