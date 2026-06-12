from pathlib import Path 

path = Path('my_folder/file1.txt')

if path.exists():
    print("The path exists.")
    print(path.name)#returns the file name:
    print(path.parent)#returns the parent directory
    print(path.stem) # file1
    print(path.suffix)# .txt
    path.write_text("New line")
    content= path.read_text()
    print(content)
    
else:
    print("The path does not exist.")
