import re

text = "John has a cat named mittens"

animal_pattern = r'(\w+) has a (\w+) named (\w+)'
match = re.search(animal_pattern,text)

if match:
    animal_type = match.group(2)
    animal_name = match.group(3)
    new_text = re.sub(animal_pattern,f'{animal_type.capitalize()} named {animal_name.capitalize()} beloongs to \\g<1>',text)
    print(new_text)
else:
    print("Invalid")

"""
\\<g1> means John
(John) has a (cat) named (Mittens)
   1            2            3
"""