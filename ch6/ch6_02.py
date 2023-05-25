def length(txt):
    if txt == '':
        return 0
    else:
        # a = 1 + length(txt[1:]) #olleh
        a = 1 + length(txt[:-1])  # hello
        if a % 2 == 1:
            print(txt[-1:], end='')
            print('*', end='')
        elif a % 2 == 0:
            print(txt[-1:], end='')
            print('~', end='')
        if txt == inp:
            print()
        return a
        # return 1 + length(txt[1:])


inp = input('Enter Input : ')
print(length(inp))
