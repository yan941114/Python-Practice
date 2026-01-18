total = []
while True:
    price = int(input())
    if price == -1:
        break
    total.append(price)
print("Total: %d"% sum(total))
if sum(total) > 1000:
    print("final: %d"% (sum(total) * 0.9))
else:
    print("final: %d"% sum(total))