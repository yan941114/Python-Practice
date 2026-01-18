password = input()
shift = int(input())
for c in password:
    print(chr(ord(c) + shift), end='')