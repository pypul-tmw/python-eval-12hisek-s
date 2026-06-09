with open("name.txt","r") as name_file, open("surname.txt","r") as surname_file:
    name = name_file.readlines()
    surname = surname_file.readlines()

with open("fullname.txt","w") as f:
    for name,surname in zip(name,surname):
        f.write(name.strip() + " " +surname.strip() + "\n")