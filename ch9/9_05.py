def insertionSort(totalPoint, len, i, first):
    if i == len:
        return
    totalPointI = totalPoint[i]
    inpI = inp[i]
    gdI = gd[i]
    insert(inpI, gdI, totalPoint, totalPointI, i, first)
    insertionSort(totalPoint, len, i + 1, first)


def insert(inpI, gdI, totalPoint, totalPointI, j, first):
    if j == first - 1:
        return
    if int(totalPointI) > int(totalPoint[j-1]) and j > first:
        totalPoint[j] = totalPoint[j-1]
        inp[j] = inp[j-1]
        gd[j] = gd[j-1]
        insert(inpI, gdI, totalPoint, totalPointI, j - 1, first)
    else:
        totalPoint[j] = totalPointI
        inp[j] = inpI
        gd[j] = gdI
        return


def display(l, len, i=0):
    if i == len:
        lp = l[len].split(',')
        print('[\'', end='')
        print(lp[0], end='')
        print('\', {\'points\': ', end='')
        print(totalPoint[len], end='')
        print('}, {\'gd\': ', end='')
        print(gd[len], end='')
        print('}]')
        return
    else:
        lp = l[i].split(',')
        print('[\'', end='')
        print(lp[0], end='')
        print('\', {\'points\': ', end='')
        print(totalPoint[i], end='')
        print('}, {\'gd\': ', end='')
        print(gd[i], end='')
        print('}]')
    display(l, len, i + 1)


inp = input('Enter Input : ').split('/')
totalPoint, gd = [], []
found = False
a, first, last = 0, 0, 0
for i in range(len(inp)):
    team = inp[i].split(',')
    totalPoint.append((3*int(team[1])) + int(team[3]))
    gd.append(int(team[4]) - int(team[5]))
print('== results ==')
insertionSort(totalPoint, len(totalPoint), 1, first)
while a < len(totalPoint):
    for b in range(len(totalPoint)):
        if a != b:
            if totalPoint[a] == totalPoint[b]:
                first = a
                last = b
                found = True
    if found:
        insertionSort(gd, last + 1, first, first)
        a = last
    found = False
    a += 1
display(inp, len(inp) - 1)
