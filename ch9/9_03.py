def insertionSort(l, len, i=1):
    if i == len:
        return
    ele = l[i]
    insert(l, ele, i, i)
    insertionSort(l, len, i + 1)
    return l


def insert(l, ele, j, dis):
    if j == -1:
        return
    if int(ele) < int(l[j-1]) and j > 0:
        l[j] = l[j-1]
        insert(l, ele, j - 1, dis)
    else:
        print('insert', ele, 'at index', j, ': [', end='')
        l[j] = ele
        display(l, dis, 0)
        print(']', end=' ')
        if dis != len(l) - 1:
            print('[', end='')
            display(l, len(l) - 1, dis + 1)
            print(']')
        else:
            print()
        return


def display(l, len, i):
    if i == len:
        print(l[len], end='')
        return
    else:
        print(l[i], end='')
        print(', ', end='')
    display(l, len, i + 1)


inp = input('Enter Input : ').split()
insertionSort(inp, len(inp))
print('sorted')
print('[', end='')
display(inp, len(inp) - 1, i=0)
print(']', end='')
