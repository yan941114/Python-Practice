password = input()
if len(password) >= 8:
    if any(c.isupper() for c in password):
        if any(c.isdigit() for c in password):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")