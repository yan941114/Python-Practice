word = input().split()
word.sort()
count = 0
for w in word:
    if word.count(w) > count:
        count = word.count(w)
        most = w
print("Word: " + most)
print("Count:", count)