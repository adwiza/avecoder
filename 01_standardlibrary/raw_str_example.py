not_raw_str = 'Not\tRaw\t\nString'

# print(not_raw_str)

raw_str = r'Not\tRaw\t\nString'

# print(raw_str)

# print(r'Not\tRaw\t\nString' == 'Not\\tRaw\\t\\nString')
#
# print(len(not_raw_str))
# print(len(raw_str))
# print(list(not_raw_str))
# print(list(raw_str))

s_r = repr(not_raw_str)
s_r2 = repr(not_raw_str)[1:-1]
print(s_r2)
print(s_r)
print(list(s_r))

print(raw_str == s_r2)

print(r'\t' == repr('\t')[1:-1])