from array import array

int_array = array('i', [18, 6, 21, 20, 43, 22, 33, 60, 8, 4, 3, 16, 31, 34])

print(int_array.typecode)
print(int_array.itemsize)

int_array.insert(0, 0)
int_array.append(42)
int_array.extend([35, 36, 37])

print(int_array)

for i, elem in enumerate(int_array):
    int_array[i] = elem * 2

print(int_array)

int_array.insert(0, 8.2)    # TypeError
