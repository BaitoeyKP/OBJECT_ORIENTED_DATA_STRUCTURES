def maxIndex(a, j, i):
    if i == j:
        return i
    k = maxIndex(a, j, i + 1)
    return (i if a[i] > a[k] else k)


def selectionSort(a, n, index=0):
    if index == n:
        print('[', end='')
        display(a, len(a) - 1, i=0)
        print(']')
        return
    k = maxIndex(a, n - index - 1, i=0)
    if k != n - index - 1:
        a[k], a[n - index - 1] = a[n - index - 1], a[k]
        print('swap', a[k], '<->', a[n - index - 1], ': [', end='')
        display(a, len(a) - 1, i=0)
        print(']')
    selectionSort(a, n, index + 1)
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
selectionSort(inp, len(inp))
