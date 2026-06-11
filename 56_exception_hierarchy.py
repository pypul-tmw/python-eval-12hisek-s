def divide_numbers(a,b):
    try:
        result = a / b 
        return result
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero!",e)
    except TypeError as e:
        print("Error: Invalid type used!",e)
    except Exception as e:
        print("Some unexpected error occurred:",e)
    finally:
        print("Operation attempted.")

print(divide_numbers(10,2))#work fine
print(divide_numbers(10,0))#work fine
print(divide_numbers(10,"a"))#work fine
print(divide_numbers(None,2))#work fine
