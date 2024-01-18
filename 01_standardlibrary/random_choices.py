import random
import string

traffic_lights = ['Red', 'Yellow', 'Green']
timing = [30, 2, 15]
# print(random.choices(traffic_lights, timing, k=10))

random_letters = random.sample(string.ascii_lowercase, 10)
# print(random_letters)
players = ['John', 'Jane', 'Jenny', 'Jenifer', 'Joceline']
random.shuffle(players)
print(players)