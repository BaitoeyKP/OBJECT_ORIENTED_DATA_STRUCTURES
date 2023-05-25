print('*** Mod Position ***')
arr, s = input('Enter Input : ').split(',')


def mod_position(arr, s):
    ans = []
    for i in range(len(arr)):
        if (i+1) % int(s) == 0:
            ans.append(arr[i])
    print(ans)


mod_position(arr, s)
