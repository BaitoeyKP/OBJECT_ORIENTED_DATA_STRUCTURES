print('*** Fun with Drawing ***')
s = int(input('Enter input : '))
# UP
dl = s
pl = -1
dm = dl+dl-3
for a in range(s):  # row
    for b in range(dl-1):
        print('.', end='')
    print('*', end='')
    for c in range(0, pl):
        print('+', end='')
    if a > 0:
        print('*', end='')
    for d in range(0, dm):
        print('.', end='')
    if a < s-1:
        print('*', end='')
    for e in range(0, pl):
        print('+', end='')
    if a > 0:
        print('*', end='')
    for f in range(dl-1):
        print('.', end='')
    print()  # new row
    dl -= 1
    pl += 2
    dm -= 2
# DOWN
dr = pl+pl-2
pd = pl+pl-5
dd = 1
for h in range(dr, 0, -2):  # row
    for i in range(0, dd):
        print('.', end='')
    print('*', end='')
    for j in range(0, pd):
        print('+', end='')
    if h > 2:
        print('*', end='')
    for k in range(0, dd):
        print('.', end='')
    print()  # new row
    dd += 1
    pd -= 2
