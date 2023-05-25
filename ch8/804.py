inp = input('Enter Input : ').split('/')
power = inp[0].split()
sumPower = 0
knightPower = []
do = True
for check in range(len(power)):
    if 0 <= int(power[check]):
        do = True
    else:
        do = False
        break
while do:
    for i in range(len(power)):
        sumPower += int(power[i])
    print(sumPower)
    for i in range(len(power)):
        if i >= (len(power)-1)/2:
            knightPower.append(int(power[i]))
        elif i < (len(power)-1)/2:
            if (len(power)-1) % 2 == 0:
                knightPower.append(
                    int(power[i]) + int(power[(i*2)+1]) + int(power[(i*2)+2]))
            else:
                if i == (len(power)-1) // 2:
                    knightPower.append(int(power[i]) + int(power[(i*2)+1]))
                else:
                    knightPower.append(
                        int(power[i]) + int(power[(i*2)+1]) + int(power[(i*2)+2]))
    if len(inp) > 1:
        compare = inp[1].split(',')
        for j in range(len(compare)):
            c = compare[j].split()
            if 0 <= int(c[0]) < len(power) and 0 <= int(c[1]) < len(power):
                if knightPower[int(c[0])] < knightPower[int(c[1])]:
                    print(c[0], end='')
                    print('<', end='')
                    print(c[1])
                elif knightPower[int(c[0])] == knightPower[int(c[1])]:
                    print(c[0], end='')
                    print('=', end='')
                    print(c[1])
                elif knightPower[int(c[0])] > knightPower[int(c[1])]:
                    print(c[0], end='')
                    print('>', end='')
                    print(c[1])
    break
