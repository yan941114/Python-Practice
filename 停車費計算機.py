min = int(input())
if min <= 30:
    print(0)
elif min <= 120:
    if min % 30 == 0:
        print((min / 30) * 20)
    else:
        print((min // 30 + 1) * 20)
else:
    if min % 30 == 0:
        price = (80 + ((min - 120) // 30) * 30)
    else:
        price = (80 + ((min - 120) // 30 + 1) * 30)
    if price >= 300:
        print(300)
    else:
        print(price)