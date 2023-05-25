class funString():
    def __init__(self, s1):
        self.s1 = s1

    def size(self):
        return len(self.s1)

    def changeSize(self):
        ul = ''
        for i in range(len(self.s1)):
            ac = ord(self.s1[i])  # ord() char to num
            if 64 < ac < 91:
                ac += 32
                ul += chr(ac)  # chr() num to char
            elif 96 < ac < 123:
                ac -= 32
                ul += chr(ac)
        return ul

    def reverse(self):
        rv = ''
        for j in range(len(self.s1), 0, -1):
            rv += self.s1[j-1]
        return rv

    def deleteSame(self):
        ds = ''
        status = 1
        c = 0
        for a in range(len(self.s1)):
            for b in range(len(ds)):
                if self.s1[b] == self.s1[a]:
                    status = 0
                    break
                else:
                    status = 1
            if status == 1:
                ds += self.s1[c]
            status = 0
            c += 1
        return ds


s1, s2 = input("Enter String and Number of Function : ").split(' ')
res = funString(s1)
if s2 == "1":
    print(res.size())
elif s2 == "2":
    print(res.changeSize())
elif s2 == "3":
    print(res.reverse())
elif s2 == "4":
    print(res.deleteSame())
