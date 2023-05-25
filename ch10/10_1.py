def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if int(arr[mid]) == int(x):
            return mid
        elif int(arr[mid]) > int(x):
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1


inp = input('Enter Input : ').split('/')
arr = inp[0].split()
result = binarySearch(sorted(arr), 0, len(arr)-1, inp[1])
if result != -1:
    print('True')
else:
    print('False')
