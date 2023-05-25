def min_elemnt(inp, len):
    if len == 1:
        return inp[0]
    return min(inp[len-1], min_elemnt(inp, len-1))


inp = list(map(int, input('Enter Input : ').split()))
len = len(inp)
print('Min :', min_elemnt(inp, len))
