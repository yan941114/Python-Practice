num = int(input("請輸入一個數字: "))
result = 0
for i in range(1, num + 1):
    if i % 13 == 0:
        result += i
print("從1到%d的總和是: %d"%(num, result))