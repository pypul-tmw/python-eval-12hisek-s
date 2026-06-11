from itertools import compress

names = ["Alice","Bob","Charlie","David"]
selectors = [1,0,1,0]

list1 = list(compress(names,selectors))
print(list1)

""" 
| name    | selector | keep? |
| ------- | -------- | ----- |
| Alice   | 1        | yes   |
| Bob     | 0        | no    |
| Charlie | 1        | yes   |
| David   | 0        | no    |

"""