times = int(input())
for i in range(times):
    num = input()
    total = 0
    for i in num:
        total += int(i)
    print("Sum of all digits of %s is %d" % (num, total))