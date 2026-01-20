num1 = []
num2 = []
print("Create tuple1:")
while True:
    num = int(input())
    if num == -9999:
        break
    num1.append(num)
print("Create tuple2:")
while True:
    num = int(input())
    if num == -9999:
        break
    num2.append(num)
combined = num1 + num2
print("Combined tuple before sorting:", tuple(combined))
print("Combined list after sorting:", sorted(combined))