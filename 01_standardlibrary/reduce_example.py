from functools import reduce


def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)

    return value


def ave_add(a, b):
    result = a + b
    print(f'{a} + {b} = {result}')
    return result


# print(ave_add(2, 3))

nums = [1, 2, 3, 4, 5]

# print(reduce(ave_add, nums))
# Initializer
# print(reduce(ave_add, nums, 1000))

# print(reduce(lambda a, b: a + b, nums, 1000))

from operator import add

# print(add(2, 3))
#
# print(reduce(add, nums))
#
# print(sum(nums))


def ave_mult(product, nums):
    for num in nums:
        product *= num

    return product


def ave_mult(a, b):
    return a * b


# print(reduce(ave_mult, nums))
# print(reduce(lambda a, b: a * b, nums))

from operator import mul

# print(mul(4, 5))

# print(reduce(mul, nums))

from timeit import timeit


def add(a, b):
    return a + b


ave_add = 'functools.reduce(add, range(100))'
print(timeit(ave_add, 'import functools', globals={'add': add}))

ave_lambda = "functools.reduce(lambda x, y: x + y, range(100))"
print(timeit(ave_lambda, "import functools"))

operator_add = "functools.reduce(operator.add, range(100))"
print(timeit(operator_add, "import functools, operator"))

print(timeit("sum(range(100))", globals={'sum': sum}))