num = int(input())
if num % 3 == 0:
    if num % 8 == 0:
        print("%d 是 3 及 8 的倍數"% num)
    else:
        print("%d 是 3 的倍數"% num)
else:
    if num % 8 == 0:
        print("%d 是 8 的倍數"% num)
    else:
        print("%d 不是 3 也不是 8 的倍數"% num)