import random

print(random.random())
print(random.random())
print(random.random())

for i in range(10):
    if random.random() <= .5:
        print('Heads')
    else:
        print('Tails')

print(random.uniform(1, 100))
print(random.randint(1, 100))
print(random.randrange(0, 101, 5))

random.seed(1)

print(random.random())
print(random.random())

print('***' * 20)

random.seed(1)
print(random.random())
print(random.random())

print('***' * 20)
