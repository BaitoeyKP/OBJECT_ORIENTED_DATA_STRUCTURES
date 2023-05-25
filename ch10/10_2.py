def firstGreaterValue(arr, l, r, key):
    mid = l + (r - l) // 2
    if l == r:
        if r == len(arr) - 1:
            return 'No First Greater Value'
        else:
            return arr[mid]
    if arr[mid] <= key:
        return firstGreaterValue(arr, mid + 1, r, key)
    elif arr[mid] > key:
        return firstGreaterValue(arr, l, mid, key)


inp = input('Enter Input : ').split('/')
arr = list(map(int, inp[0].split()))
key = inp[1].split()
for i in range(len(key)):
    print(firstGreaterValue(sorted(arr), 0, len(arr) - 1, int(key[i])))
