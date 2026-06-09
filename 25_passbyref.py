def append_to_list(lst):
    lst.append(1)
    return lst

a = [5]
b = append_to_list(a)

print(a)
print(b)