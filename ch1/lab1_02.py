print(' *** Wind classification ***')
w = float(input("Enter wind speed (km/h) : "))
if 0 < w < 51.99:
    print('Wind classification is Breeze.')
elif 52.00 < w < 55.99:
    print('Wind classification is Depression.')
elif 56.00 < w < 101.99:
    print('Wind classification is Tropical Storm.')
elif 102.00 < w < 208.99:
    print('Wind classification is Typhoon.')
elif w >= 209:
    print('Wind classification is Super Typhoon.')
else:
    print('error')
