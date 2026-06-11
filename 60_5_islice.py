from itertools import islice 

nums = range(100)

list1 = list(islice(nums,5,10)) # islice(variable,start,end)
print(list1)