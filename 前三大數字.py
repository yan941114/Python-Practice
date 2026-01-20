num = []
top3 = []
for i in range(10):
    num.append(int(input()))
num.sort(reverse=True)
for j in range(3):
    top3.append(num[j])
print("%d %d %d" % (top3[0], top3[1], top3[2]))