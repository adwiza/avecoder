import math
from functools import reduce
from itertools import filterfalse

nums = [-5, 0, 1, 3, -4, -6, 9, -7, 2, 4, 5]


def filter_negatives(nums):
    neg_nums = []
    for num in nums:
        if num < 0:
            neg_nums.append(num)
    return neg_nums


def is_negative(num):
    return num < 0


neg_nums = filter(lambda x: x < 0, nums)

# filter + map
neg_nums2 = filter(is_negative, nums)


# filterfalse()

if __name__ == '__main__':
    # print(filter_negatives(nums))
    # print(list(neg_nums))
    # print(list(neg_nums2))
    # print(list(map(lambda n: math.sqrt(math.pow(n, 2)), list(neg_nums))))
    # print(list(map(lambda n: math.sqrt(math.pow(n, 2)),  filter(is_negative, nums))))
    # print(reduce(lambda a, b: a * b, neg_nums))
    # print(reduce(lambda a, b: a * b, filter(is_negative, nums)))
    print(list(filterfalse(is_negative, nums)))