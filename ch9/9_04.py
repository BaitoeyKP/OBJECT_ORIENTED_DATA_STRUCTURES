def bubbleSort(a, i, j, n, l):
    if j == n:
        i = i+1
        j = 0
    if i == n:
        return
    if a[i] < a[j]:
        temp = a[j]
        a[j] = a[i]
        a[i] = temp
        temp = l[j]
        l[j] = l[i]
        l[i] = temp
        bubbleSort(a, i, j + 1, n, l)
    else:
        bubbleSort(a, i, j + 1, n, l)
    return l


def display(l, len, i):
    if i == len:
        print(l[len], end='')
        return
    else:
        print(l[i], end='')
        print(' ', end='')
    display(l, len, i + 1)


inp = input('Enter Input : ').split()
l = []
for i in range(len(inp)):
    a = inp[i]
    for j in range(len(a)):
        if 'a' <= a[j] <= 'z':
            l.append(a[j])
display(bubbleSort(l, 0, 0, len(inp), inp), len(inp)-1, i=0)
