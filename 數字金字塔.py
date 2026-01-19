layer = int(input())
for i in range(layer):
    print(" " * (layer - (i + 1)) * 2, end="")
    for j in range(i + 1):
        print(j + 1, end=" ")
    print()