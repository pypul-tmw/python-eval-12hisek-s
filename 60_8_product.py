from itertools import product

for item in product([1,2],["A","B"]):
    print(item)


""" 
Same as:
for x in[ 1,2]:
    for y in ['A','B]:
        print((x,y))
"""