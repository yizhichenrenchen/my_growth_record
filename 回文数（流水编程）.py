i = -121
i1 = str(i)
i2 = i1[::-1]
i3 = int(i2)
if i < 0:
    print('False')
    if i == i3:
        print('True')
    else:
        print('False')