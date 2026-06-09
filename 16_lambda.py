from functools import reduce
numbers = [1,2,3,4,5,6]
#using map function
square = list(map(lambda x:x**2,numbers))
print("Using map function")
print(square)

#using filter function
evens = list(filter(lambda x: x % 2 == 0,numbers))
print("Using filter function")
print(evens)

#using reduction function
#reduce(): This function repeatedly applies a lambda expression to elements of a list to combine them into a single result.
product = list(reduce(lambda x,y: x * y,numbers))
print("Using reduce function")
print(product)