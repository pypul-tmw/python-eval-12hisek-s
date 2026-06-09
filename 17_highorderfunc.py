def apply_to_each(func,iterable):
    return [func(x) for x in iterable]

def square(x):
    return x*x

numbers = [1,2,3,4,5]

squared_numbers = apply_to_each(square,numbers)
print(squared_numbers)



"""
#using map
squared_numbers = list(map(square,numbers))
"""
