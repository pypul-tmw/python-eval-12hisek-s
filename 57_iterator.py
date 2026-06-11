class EvenNumbers:
    def __init__(self, limit):
        self.current = 2
        self.limit = limit
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        
        value = self.current
        self.current += 2
        return value

for num in EvenNumbers(10):
    print(num)