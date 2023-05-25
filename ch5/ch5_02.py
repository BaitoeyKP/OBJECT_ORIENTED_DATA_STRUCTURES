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
        while p != None:
            print(p.data, end='')
            if p.next != None:
                print('->', end='')
            else:
                print()
            p = p.next

    def str_reverse(self):
        prev = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def remove(self, data):
        p = self.head
        index = -1
        if (p is not None):
            if (p.data == data):
                self.head = p.next
                p = None
                index += 1
                print('removed :', data, 'from index :', index)
                return
        while (p is not None):
            index += 1
            if p.data == data:
                print('removed :', data, 'from index :', index)
                break
            prev = p
            p = p.next
        if (p == None):
            return
        prev.next = p.next
        p = None

    def insertAtHead(self, data):
        p = Node(data)
        if ans.isEmpty():
            self.head = p
            self.tail = p
        else:
            current = self.head
            p.next = self.head
            current.previous = p
            self.head = p
            while current.next != None:
                current = current.next
            self.tail = current

    def checkData(self, data):
        p = self.head
        while p != None:
            if p.data == data:
                return True  # data found
            p = p.next
        return False  # Data Not found


inp = input('Enter Input : ').split(',')
ans = LinkedList()
for i in range(len(inp)):
    order = inp[i].split()
    if order[0] == 'A':
        ans.append(order[1])
    elif order[0] == 'Ab':
        ans.insertAtHead(order[1])
    elif order[0] == 'I':
        add = order[1].split(':')
        index = int(add[0])
        data = add[1]
        if index < 0:
            print('Data cannot be added')
        else:
            ans.insert(data, index)
    elif order[0] == 'R':
        # or no data
        if ans.isEmpty() == True or ans.checkData(order[1]) == False:
            print('Not Found!')
        else:
            ans.remove(order[1])
    print('linked list : ', end='')
    if ans.isEmpty() == True:
        print()
    else:
        ans.printList()
    ans.str_reverse()
    print('reverse : ', end='')
    if ans.isEmpty() == True:
        print()
    else:
        ans.printList()
    ans.str_reverse()
