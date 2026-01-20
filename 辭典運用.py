key = []
value = []
dic = {}
while True:
    key_input = input("Key: ")
    if key_input == "end":
        break
    key.append(key_input)
    value.append(input("Value: "))
    dic = dict(zip(key, value))
search = input("Search key: ")
print(search in dic)