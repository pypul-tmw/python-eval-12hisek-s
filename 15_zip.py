# The zip function is used to combine two or more iterables into a single iterable.

fruits = ["apple","banana","cherry"]
colors = ["red","yellow","red"]
for fruit,color in zip(fruits,colors):
    print(fruit,color)