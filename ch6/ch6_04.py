def move(n, A, C, B, s):
    if n == 1:
        print('move 1 from ', A, 'to', C)
        z = ' ' + str(n)
        if A == 'A':
            if z in a:
                a[a.index(z)] = '|'
            else:
                a[a.index(n)] = '|'
        elif A == 'B':
            if z in b:
                b[b.index(z)] = ' |'
            else:
                b[b.index(n)] = ' |'
        elif A == 'C':
            if z in c:
                c[c.index(z)] = ' |'
            else:
                c[c.index(n)] = ' |'
        dis(C, t, 1, n)
        print('|  |  |')
        display(t, s, a, b, c)
        return
    move(n - 1, A, B, C, s)
    print('move', n, 'from ', A, 'to', C)
    z = ' ' + str(n)
    if A == 'A':
        if z in a:
            a[a.index(z)] = '|'
        else:
            a[a.index(n)] = '|'
    elif A == 'B':
        if z in b:
            b[b.index(z)] = ' |'
        else:
            b[b.index(n)] = ' |'
    elif A == 'C':
        if z in c:
            c[c.index(z)] = ' |'
        else:
            c[c.index(n)] = ' |'
    dis(C, t, 1, n)
    print('|  |  |')
    display(t, s, a, b, c)
    move(n - 1, B, C, A, s)


def dis(C, t, e, n):
    if e == t:
        if C == 'C':
            c[len(c)-e] = ' ' + str(n)
        elif C == 'B':
            b[len(b)-e] = ' ' + str(n)
        elif C == 'A':
            a[len(a)-e] = n
        return
    if C == 'C':
        if c[len(c)-e] == ' |' or c[len(c)-e] == '|':
            c[len(c)-e] = ' ' + str(n)
        else:
            dis(C, t, e+1, n)
    elif C == 'B':
        if b[len(b)-e] == ' |' or b[len(b)-e] == '|':
            b[len(b)-e] = ' ' + str(n)
        else:
            dis(C, t, e+1, n)
    elif C == 'A':
        if a[len(a)-e] == ' |' or a[len(a)-e] == '|':
            a[len(a)-e] = n
        else:
            dis(C, t, e+1, n)


def display(n, s, a, b, c):
    if s == n:
        if len(a) < n and len(b) < n and len(c) < n:
            a.append(s)
            b.append(' |')
            c.append(' |')
        print(a[s-1], b[s-1], c[s-1])
        return
    if len(a) < n and len(b) < n and len(c) < n:
        a.append(s)
        b.append(' |')
        c.append(' |')
    print(a[s-1], b[s-1], c[s-1])
    display(n, s+1, a, b, c)


n = int(input("Enter Input : "))
a, b, c = [], [], []
s = 1
t = n
print('|  |  |')
display(n, s, a, b, c)
move(n, 'A', 'C', 'B', s)
