num1 = int(input())
num2 = int(input())
i = 1
while i <= num1 and i <= num2:
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
    i += 1
print("GCD: {:<10}".format(gcd))
while i <= num1 * num2:
    if i % num1 == 0 and i % num2 == 0:
        lcm = i
        break
    i += 1
print("LCM: {:<10}".format(lcm))