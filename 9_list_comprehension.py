numbers = [10,23,11,12,2,74]
"""
#using loop
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
        print(even_numbers)
"""
#using list comprehension

even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)


square_numbers = [number ** 2 for number in numbers ]
print(square_numbers)