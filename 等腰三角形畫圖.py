layer = int(input())
for i in range(layer):
    for j in range(1, layer - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()