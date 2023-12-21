import pprint

ave_data = [{'Strings': 'One', 'Integers': 10, 'Floats': [4.24, 42.6]},
            {'Strings': 'Two', 'Integers': 20, 'Floats': [6.43, 65.2]},
            {'Strings': 'Three', 'Integers': 30, 'Floats': [9.87, 8.81]}
            ]


# print(ave_data)
# pprint.pprint(ave_data)
# pprint.pprint(ave_data, width=39)
# pprint.pprint(ave_data, depth=2)
# pprint.pprint(ave_data, depth=3)
# pprint.pprint(ave_data, indent=3)

ave_more_data = [list(range(10)), list(range(100, 120))]

# print(ave_more_data)
# pprint.pprint(ave_more_data, width=45)
# pprint.pprint(ave_more_data, width=45, compact=True)

# print(ave_data)
# print(type(ave_data))
#
# str_ave_data = str(ave_data)
# print(str_ave_data)
# print(type(str_ave_data))

pp_ave_data = pprint.pformat(ave_data)

# print(pp_ave_data)
# print(type(pp_ave_data))

print(pprint.pformat(ave_data, depth=2, width=45, indent=2))