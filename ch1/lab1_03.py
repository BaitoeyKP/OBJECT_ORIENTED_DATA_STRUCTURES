print('*** Reading E-Book ***')
s = input('Text , Highlight : ').split(',')
i = 0
while i < len(s[0]):
    # print(s[1], s[0][i:i+len(s[1])])
    if s[1] == s[0][i:i+len(s[1])]:
        print('[' + s[0][i:i+len(s[1])] + ']', end='')
        i += len(s[1])
    else:
        print(s[0][i], end='')
        i += 1
