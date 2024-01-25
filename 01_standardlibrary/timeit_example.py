# timeit.timeit(stmt, setup, timer, number)

import timeit
# print(timeit.timeit('Output = 10*5'))

########
import_module = 'import random'
testcode = '''
def test():
    return random.randint(10, 1000)
'''

print(timeit.timeit(stmt=testcode, setup=import_module))
print(timeit.repeat(stmt=testcode, setup=import_module, repeat=5))

