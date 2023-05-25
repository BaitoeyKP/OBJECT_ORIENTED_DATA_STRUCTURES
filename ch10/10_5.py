inp = input('Enter Input : ').split('/')
w = inp[0]
k = inp[1]
n = []
for e in w.split():
    n.append(int(e))
data = n
k = int(k)
l = n[0]
r = 100
while l != r:
    mid = int((l + r) / 2)
    box = []
    status = False
    for i in range(k):
        box.append(mid)
    j = 0
    for i in data:
        while j < k and box[j] < i:
            j += 1
        if j >= k:
            l = mid + 1
            status = True
            break
        box[j] -= i
    if not status:
        r = mid
print('Minimum weigth for {0} box(es) = {1}'.format(k, l))
