while True:
    times = input()
    try:
        times = int(times)
        if times >= 1 and times <= 100:
            break
        print("請輸入1~100的整數")
        continue
    except:
        print("請輸入1~100的整數")
for i in range(times):
    nums = [float(j) for j in input().split()]
    print("%.2f" % (max(nums) - min(nums)))