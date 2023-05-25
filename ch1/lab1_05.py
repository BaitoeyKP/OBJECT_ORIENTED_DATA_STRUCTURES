print('*** Fun with countdown ***')
l = input('Enter List : ').split(' ')
c = 0
ans = []
a = 0
f = 0
aAns = []
for i in range(len(l)):
    if int(c)-int(l[i]) == 1 or int(l[i]) == 1:
        if f == 0:
            ans.append(c)
            f = 1
        ans.append(l[i])
        if int(l[i]) == 1:
            a += 1
    elif int(c)-int(l[i]) != 1:
        ans.clear
        f = 0
    c = l[i]
for z in range(len(ans)):
    if ans[z] == 0:
        ans.remove(0)
        break
aj = a
aAns.append(a)
for an in range(len(aAns)):
    if an == 0:
        print('[', end='')
    print(aAns[an], end='')
    print(', ', end='')
for j in range(len(ans)):
    if j == 0:
        print('[[', end='')
    print(ans[j], end='')
    if ans[j] == '1' and aj == 1:
        print(']]', end='')
    elif ans[j] == '1' and aj > 1:
        print('], [', end='')
        aj -= 1
    elif ans[j] != '1':
        print(', ', end='')
print(']')
