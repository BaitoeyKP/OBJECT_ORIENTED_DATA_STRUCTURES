num = input('Enter Your List : ').split(' ')
list = []
ans = []


def sumArray(num):
    if len(num) < 3:
        print('Array Input Length Must More Than 2')
    else:
        for a in range(len(num)):
            list.append(num[a])
        for i in range(len(list)):
            for j in range(len(list)):
                for k in range(len(list)):
                    if int(list[i])+int(list[j])+int(list[k]) == 0 and i != j and i != k and j != k:
                        # and int(list[i]) != int(list[j]) \
                        # and int(list[i]) != int(list[j]) and int(list[j]) != int(list[k]):
                        ans.append(list[i])
                        ans.append(list[j])
                        ans.append(list[k])

        fAns = []
        st = 1
        y = 0
        for c in range(len(ans)):
            for d in range(len(fAns)):
                if ans[c] == fAns[d]:
                    st = 0
                    if ans[c] == '0' and c < 3:
                        st = 1
                    break
                else:
                    st = 1
            if st == 1:
                fAns.append(ans[y])
            st = 0
            y += 1

        print('[', end='')
        for x in range(len(fAns)):
            if x == 0:
                print('[', end='')
            print(fAns[x], end='')
            if (x+1) % 3 != 0:
                print(', ', end='')
            elif (x+1) % 3 == 0:
                print(']', end='')
                if x+1 != len(fAns):
                    print(', [', end='')
        print(']', end='')


sumArray(num)
