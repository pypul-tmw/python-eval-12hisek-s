def even_numbers(limit):
    current = 2

    while current <= limit:
        yield current
        current += 2

for num in even_numbers(10):
    print(num)

"""
| Iterator                | Generator                       |
| ----------------------- | ------------------------------- |
| Need `__iter__()`       | Uses `yield`                    |
| Need `__next__()`       | Python creates it automatically |
| More code               | Less code                       |
| Manual state management | Automatic state management      |
"""