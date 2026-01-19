matrix = [[], [], []]
for i in range(3):
    for j in range(3):
        matrix[i].append(int(input()))
print("Main Sum: %d" % (matrix[0][0] + matrix[1][1] + matrix[2][2]))
print("Sub Sum: %d" % (matrix[0][2] + matrix[1][1] + matrix[2][0]))