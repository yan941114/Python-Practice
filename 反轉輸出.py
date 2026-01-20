num = input()
length = len(str(num))
for i in range(length):
    n = num[length - i - 1]
    print(n, end="")