import cProfile


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


# for i in infinite_sequence():
#     if i < 1000:
#         print(i)


file_name = ('huge_csv.csv')


def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split('\n')
    return result


def csv_reader2(file_name):
    for row in open(file_name, "r"):
        yield row


# cProfile.run('sum([num ** 2 for num in range(1000000)])')
# cProfile.run('sum((num ** 2 for num in range(1000000)))')


def print_strings():
    yield_str = 'aaaaaaaaaaaaaaaaaaa'
    yield yield_str
    yield_str = 'bbbbbbbbbbbbbbbbbbb'
    yield yield_str
    yield_str = 'ccccccccccccccccccc'
    yield yield_str


iter_print_strings = print_strings()

# print(next(iter_print_strings))
# print(next(iter_print_strings))
# print(next(iter_print_strings))

chars = ['a', 'b', 'c', 'd', 'e']

it = iter(chars)

# while True:
#     try:
#         letter = next(it)
#     except StopIteration:
#         print('that is all')
#         break
#     print(letter)


def is_palindrome(num):
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False


def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1


if __name__ == '__main__':
    pal_gen = infinite_palindromes()

    for i in pal_gen:
        digits = len(str(i))
        if digits == 10:
            # pal_gen.throw(ValueError('Too long'))
            pal_gen.close()
        pal_gen.send(10 ** (digits))
        print(i )
