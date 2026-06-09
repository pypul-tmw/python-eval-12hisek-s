#mutable data types
#list
list = [1,2,3]
list2 = list
list[0] = 0
print(list)
print(list2)

#Dict
dict = {'key1':'value1','key2':'value2'}
dict2 = dict
dict['key2'] = "new_val2"
print(dict)
print(dict2)


#immutable data types
#integer
a = 5
b = a
a += 1
print(a)
print(b)

#string
a = 'hello'
b = a
a += ' world'
print(a)  # 'hello world'
print(b)  # 'hello'