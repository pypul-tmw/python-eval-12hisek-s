from itertools import chain

nums = chain([1,2],["Bob","Ash"],[4,5])

for n in nums:
    print(n)