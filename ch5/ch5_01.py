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

    def __str__(self):
        return str(self.head)

    def append(self, data):
        p = Node(data)
        if self.head == None:  # null list
            self.head = p
            return
        t = self.head
        while t.next != None:
            t = t.next
        t.next = p

    def size(self):
        temp = self.head
        count = 0
        # Loop end when linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count

    def insert(self, data, index):
        p = Node(data)
        if index < 0 or index > ans.size():
            print('Data cannot be added')
        elif index == 0:
            print('index =', index, 'and data =', data)
            p.next = self.head
            self.head = p
        else:
            print('index =', index, 'and data =', data)
            new = self.head
            for i in range(0, index-1):
                if new != None:
                    new = new.next
            if new != None:
                p.next = new.next
                new.next = p

    def isEmpty(self):
        current_node = self.head
        return current_node == None

    def printList(self):
        p = self.head
        print('link list : ', end='')
        while p != None:
            print(p.data, end='')
            if p.next != None:
                print('->', end='')
            else:
                print()
            p = p.next


inp = input('Enter Input : ').split(',')
first = inp[0].split()
ans = LinkedList()
for i in range(len(first)):
    ans.append(first[i])
if ans.isEmpty() == True:
    print('List is empty')
else:
    ans.printList()
for j in range(1, len(inp)):
    add = inp[j].split(':')
    index = int(add[0])
    data = add[1]
    ans.insert(data, index)
    if ans.isEmpty() == True:
        print('List is empty')
    else:
        ans.printList()
