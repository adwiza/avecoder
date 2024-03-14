
import copy

list_one = [[1, 2, 3], [4, 5, 6], [7, 8, 'x']]
list_two = list_one

list_two[2][2] = 9

print('List One: ', list_one)
print('ID of List One: ', id(list_one))

print('List Two: ', list_two)
print('ID of List One: ', id(list_two))


######### SHALLOW ##############

list_one = [[1, 2, 3], [4, 5, 6], [7, 8, 'x']]
list_two = copy.copy(list_one)

list_one.append([10, 11, 12])

print('######### SHALLOW ##############')
print('List One: ', list_one)
print('List Two: ', list_two)

list_one[3][2] = 'X'

print('List One: ', list_one)
print('List Two: ', list_two)


######### DEEP COPY #############

list_one = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_two = copy.deepcopy(list_one)

print('Deep List One: ', list_one)
print('Deep List Two: ', list_two)

list_one[0][1] = 'Y'

print('Deep List One: ', list_one)
print('Deep List Two: ', list_two)