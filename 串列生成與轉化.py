n = int(input("請輸入欲產生的個數: "))
list_num = []
for i in range(n):
    num = int(input("請輸入第%d個數字: "% (i+1)))
    list_num.append(num)
list_num.sort(reverse=False)
print(list_num)
print(tuple(list_num))
print(set(list_num))