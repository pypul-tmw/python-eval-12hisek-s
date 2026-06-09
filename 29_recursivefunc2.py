def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)

print(sum_n(5))

"""
Procss:
sum_n(5)
= 5 + sum_n(4)
= 5 + (4 + sum_n(3))
= 5 + (4 + (3 + sum_n(2)))
= 5 + (4 + (3 + (2 + sum_n(1))))
= 5 + (4 + (3 + (2 + (1 + sum_n(0)))))
= 5 + 4 + 3 + 2 + 1 + 0
= 15
"""