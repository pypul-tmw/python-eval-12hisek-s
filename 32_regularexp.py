import re
text = 'Hello 123 World 456 Hello World'

# match any character except a newline
if re.search('. World', text):
    print('1.Match found!')
else:
    print('1.No match found.')

# match the start of a string
# No match found because string starts with "Hello"
if re.search('^World',text):
    print('2.Match found!')
else:
    print('2.No match found.')

# match the end of a string
if re.search('Hello World$', text):
    print('3.Match found!')
else:
    print('3.No match found.')

# match any character within the square brackets
if re.search('[0123456789]', text):
    print('4.Match found!')
else:
    print('4.No match found.')

# match any character not within the square brackets(hello...)
if re.search('[^0123456789]', text):
    print('5.Match found!')
else:
    print('5.No match found.')

# match any character not within the square brackets
#match = re.search(r'\w+', text)

if re.search(r'\w+', text):
    print("6.Match found!")
    #print("Matched text:", match.group())
else:
    print("6.No match found.")

#match any decimal digit
if re.search('\d+',text):
    print("7.Match found!")
else:
    print("7.No match found.")

#match any whitespace character
if re.search('\s+',text):
    print("8.Match found!")
else:
    print("8.No match found.")

# match a word boundary
if re.search(r'\bHello\b', text):
    print("9.Match found!")
else:
    print("9.No match found.")

#match either the expression before or after the symbol
if re.search('Hello World|Hello 789', text):
    print("10.Match found!")
else:
    print("10.No Match found!")


# match the start of the string
if re.search(r'\AHello',text):
    print("11.Match found!")
else:
    print("11.No match found.")


