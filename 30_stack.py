#Stack overflow is a common software programming error that occurs when a program exceeds the maximum amount of memory that is allocated for its execution

def function1(n):
    if n <= 0:
        return
    else:
        print(f'Function 1 called with n = {n}')
        function2(n - 1)
        print(f'Returning from Function 1 with n = {n}')

def function2(n):
    if n <= 0:
        return
    else:
        print(f'Function 2 called with n = {n}')
        function3(n - 1)
        print(f'Returning from Function 2 with n = {n}')

def function3(n):
    if n <= 0:
        return
    else:
        print(f'Function 3 called with n = {n}')
        function1(n - 1)
        print(f'Returning from Function 3 with n = {n}')

function1(4)