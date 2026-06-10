class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x},{self.y})"

v1 = vector(7,9)
v2 = vector(7,10)

v3 = v1 + v2
print(v3)