from functools import reduce
from math import factorial
from timeit import timeit

# non recursive case
# def factorial(num):
#     return_value = 1
#     for i in range(2, num + 1):
#         return_value *= i
#     return return_value

# recursive case
# def factorial(num):
#     return 1 if num <= 1 else num * factorial(num - 1)

# def factorial(num):
#     print(f'call factorial() wit num == {num}')
#     return_value = 1 if num <= 1 else num * factorial(num - 1)
#     print(f'factorial({num}) returned {return_value}')
#     return return_value


# def factorial(num):
#     return reduce(lambda a, b: a * b, range(1, num + 1) or [1])

### recursive
stmt = '''def factorial(num):
            return 1 if num <= 1 else num * factorial(num -1)
       '''
print('Recursive:', timeit('factorial(5)', setup=stmt, number=1000000))

### iterative

stmt = '''def factorial(num):
            return_value = 1
            for i in range(2, num + 1):
                return_value *= i
            return return_value
       '''
print('Iterative:', timeit('factorial(5)', setup=stmt, number=1000000))

### reduce
stmt = '''
from functools import reduce
def factorial(num):
    return reduce(lambda a, b: a * b, range(1, num + 1) or [1])
'''

print('Reduce:', timeit('factorial(5)', setup=stmt, number=1000000))

### math
stmt = '''
from math import factorial
        '''
print('Math:', timeit('factorial(5)', setup=stmt, number=1000000))

# if __name__ == '__main__':
#     print(factorial(5))