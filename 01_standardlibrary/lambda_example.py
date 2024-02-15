def func(x):
    return x + x


lambda x: x + x

# print((lambda x: x * 2)(14))

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_obj = (lambda x: x * 2)

# print(list_obj(list_1))

list_2 = []

for x in list_1:
    temp = lambda x: x * 2
    list_2.append(temp(x))

# print(list(list_2))

str1 = 'AveCoder'
rev_upper = lambda x: x.upper()[::-1]
# print(rev_upper(str1))

is_even_list = [lambda arg=x: arg * 10 for i in range(1, 15)]
#
# for item in is_even_list:
#     print(item())

cond = lambda a, b: a if (a > b) else b

# print(cond(10, 20))

mult_list = [[12, 23, 56], [2, 6, 14, 72], [13, 5, 7, 22]]

srt_list = lambda x: (sorted(i) for i in x)

sec_lrg = lambda x, f: [y[len(y)-2] for y in f(x)]
res = sec_lrg(mult_list, srt_list)
print(res)
