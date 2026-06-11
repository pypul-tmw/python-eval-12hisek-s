try:
    age = int(input("Enter your age:"))
except ValueError:
    print("Error: Invalid input!")

else:
    if age < 0:
        print("Error: Age cannot be negative!")
    else:
        print('Your age is:', age)