import math
n, s = int(input()), float(input())
area = (n*s**2)/(4*math.tan(math.pi/n))
print("Area = %.4f"%area)