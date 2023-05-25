class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        current, s = self.head, str(self.head.data) + ' '
        while current.next != None:
            s += str(current.next.data) + ' '
            current = current.next
        return s

    def isEmpty(self):
        current_node = self.head
        return current_node == None

    def insertAtHead(self, data):
        new = Node(data)
        if lst.isEmpty():
            self.head = new
            self.tail = new
        else:
            current = self.head
            new.next = self.head
            current.previous = new
            self.head = new
            while current.next != None:
                current = current.next
            self.tail = current

    def append(self, data):
        new = Node(data)
        if self.isEmpty():
            self.head = new
            self.tail = new
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new
            new.previous = self.tail
            self.tail = new

    def insert(self, index, data):
        new = Node(data)
        if lst.isEmpty():
            self.head = new
            self.tail = new
        else:
            current = self.head
            if index < 0:
                self.insertAtHead(new.data)
                return
            else:
                for _ in range(index):
                    current = current.next
            new.next = current.next
            new.previous = current
            current.next = new
            current = new
            if current.next != None:
                current = current.next
                current.previous = new
            while current.next != None:
                current = current.next
            self.tail = current

    def index(self, data):
        n = 0
        if self.isEmpty():
            return -1
        else:
            current = self.head
            while current:
                if str(current.data) == str(data):
                    return n
                else:
                    current = current.next
                    n += 1
            return -1

    def size(self):
        temp = self.head
        count = 0
        # Loop end when linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count

    def pop(self, index):
        current = self.head
        if index == 0:
            if current.next == None:
                self.head = None
                self.tail = None
            else:
                self.head = current.next
        else:
            for i in range(index-1):
                current = current.next
            current.next = current.next.next


inp = input('Enter Input : ').split(',')
lst = LinkedList()
cursor = '|'
lst.append(cursor)
for i in range(len(inp)):
    if len(inp[i]) > 1:
        command, word = inp[i].split()
    else:
        command = inp[i]
    if command == 'I':
        lst.insert(lst.index(cursor) - 1, word)
    elif command == 'L':
        posCursor = lst.index(cursor)
        if posCursor != 0:
            lst.pop(posCursor)
            lst.insert(posCursor - 2, cursor)
        else:
            continue
    elif command == 'R':
        posCursor = lst.index(cursor)
        if posCursor != lst.size() - 1:
            lst.pop(posCursor)
            lst.insert(posCursor, cursor)
        else:
            continue
    elif command == 'B':
        posCursor = lst.index(cursor)
        if posCursor != 0:
            lst.pop(posCursor - 1)
        else:
            continue
    elif command == 'D':
        posCursor = lst.index(cursor)
        if posCursor != lst.size() - 1:
            lst.pop(posCursor + 1)
        else:
            continue
print(lst)
