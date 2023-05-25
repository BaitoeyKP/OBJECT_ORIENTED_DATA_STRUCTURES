def bubbleSort(a, i, j, n):
    if j == n:
        i = i+1
        j = 0
    if i == n:
        return
    if a[i] < a[j]:
        temp = a[j]
        a[j] = a[i]
        a[i] = temp
        bubbleSort(a, i, j + 1, n)
    else:
        bubbleSort(a, i, j + 1, n)
    return a


def display(l, len, i):
    if i == len:
        print(l[len], end='')
        return
    else:
        print(l[i], end='')
        print(', ', end='')
    display(l, len, i + 1)


inp = input('Enter Input : ').split()
print('[', end='')
display(bubbleSort(inp, 0, 0, len(inp)), len(inp)-1, i=0)
print(']', end='')
