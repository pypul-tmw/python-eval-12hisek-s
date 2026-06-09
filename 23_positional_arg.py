#Positional-only arguments are separated with a forward slash (/) in the function definition. 
def reactangle_area(length,width,/):
    return length * width

print(reactangle_area(10,20))
print(rectangle_area(width=20, length=10)) # TypeError: rectangle_area() got some positional-only arguments passed as keyword arguments