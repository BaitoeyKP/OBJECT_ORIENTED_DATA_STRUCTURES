def power(n, p):
    if p == 0:
        return 1
    return (n*power(n, p-1))


inp = input('Enter Input a b : ').split()
n = int(inp[0])
p = int(inp[1])
print(power(n, p))
