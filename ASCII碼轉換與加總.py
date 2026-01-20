word = input()
num = []
for i in word:
    num.append(ord(i))
    print("ASCII code for '%s' is %d" % (i, ord(i)))
print(sum(num))