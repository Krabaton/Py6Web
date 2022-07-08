from functools import partial


def sum(a, b):
    return a + b


sum10 = partial(sum, b=10)
sum100 = partial(sum, b=100)
sum2on2 = partial(sum, 2, 2)

print(sum10(5))
print(sum100(5))
print(sum2on2())
