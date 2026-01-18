n = int(input())
total = 0
for i in range(n):
    num = 1/(i+1)
    total += num
print("%.4f"% total)