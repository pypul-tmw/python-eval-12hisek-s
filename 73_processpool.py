from concurrent.futures import ProcessPoolExecutor

def square(n):
    return n * n 

numbers = [1,2,3,4,5]

with ProcessPoolExecutor(max_workers=3) as executor:
    results = executor.map(square,numbers)

print(list(results))