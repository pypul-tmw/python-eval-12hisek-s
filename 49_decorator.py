def multiply_result_by(n):
    def decorator(original_function):
        def new_function(*args,**kwargs):
            result = original_function(*args,**kwargs)
            return result * n 
        return new_function
    return decorator

@multiply_result_by(2)
def my_function(x,y):
    return x + y 

print(my_function(1,2))