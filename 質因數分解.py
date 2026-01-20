num = int(input())
print("%d =" % num, end="")
i = 2
while i <= num:
    if num % i == 0:
        print(" %d" % i, end="")
        num //= i
        if num % i != 0:
            i += 1
        if num != 1:
            print(" *", end="")
    elif num == 1:
        break
    else:
        i += 1