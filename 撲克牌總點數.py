total = []
while True:
    if len(total) == 5:
        break
    point = input()
    try:
        int(point)
        if int(point) >= 2 and int(point) <= 10:
            total.append(int(point))
        else:
            print("輸入錯誤，請重新輸入")
            continue
    except ValueError:
        if point == 'J' or point == 'Q' or point == 'K':
            total.append(10)
        elif point == 'A':
            total.append(1)
        else:
            print("輸入錯誤，請重新輸入")
            continue
print(sum(total))