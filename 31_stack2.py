def large_data_structure(n,data):
    if n == 10:
        return data
    data = data + (n,)
    return large_data_structure(n+1,data)

result = large_data_structure(0,tuple())
#result2 = large_data_structure(-1000,tuple())
print(result)
#print(result2)#stack overflow