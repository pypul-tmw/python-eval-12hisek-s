names = ["Abhi","Bob","Alice"]
username = input("Enter the name:")
for name in names:
    print(f"Looking at name {name}")

    if name == username:
        print("Your name is in the list")
        break
else:
    print("Your name not in the list")