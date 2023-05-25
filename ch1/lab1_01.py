print('*** Rabbit & Turtle ***')
i = input('Enter Input : ').split(' ')
d = float(i[0])
Vr = float(i[1])
Vt = float(i[2])
Vf = float(i[3])
if d < 5000 and Vr < 5000 and Vt < 5000 and Vf < 5000 and Vt > Vr and Vf > Vr:
    t = d/(Vt-Vr)
    s = Vf*t
    print('%.2f' % s)
else:
    print('error')
