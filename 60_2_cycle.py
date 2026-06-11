from itertools import cycle

colors = cycle(["red","yellow","green"])

for _ in range(10):
    print(next(colors))