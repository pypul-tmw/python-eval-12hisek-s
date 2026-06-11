try:
    with open('myfile.txt','r') as file:
        contemts = file.read()
except FileNotFoundError:
    print("Error: File not found!")