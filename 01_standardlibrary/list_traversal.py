colours = [
    "Black",
    [
        "Gray",
        [
            "Yellow",
            "Orange",
        ],
        "Green",
        "Blue"
    ],
    "White",
    [
        "Brown",
        "Red"
    ],
    "Pink"
]


# print(len(colours))
#
# for index, item in enumerate(colours):
#     print(index, item)


# def count_leaf_items(item_list):
#     count = 0
#     stack = []
#     current_list = item_list
#     i = 0
#
#     while True:
#         if i == len(current_list):
#             if current_list == item_list:
#                 return count
#             else:
#                 current_list, i = stack.pop()
#                 i += 1
#                 continue
#         if isinstance(current_list[i], list):
#             stack.append([current_list, i])
#             current_list = current_list[i]
#             i = 0
#         else:
#             count +=1
#             i += 1

### recursion
def count_leaf_items(item_list):
    print(f'List: {item_list}')
    count = 0
    for item in item_list:
        if isinstance(item, list):
            print('if sublist')
            count += count_leaf_items(item)
        else:
            print(f'leaf item \"{item}\"')
            count += 1
    print(f'-> count is {count}')
    return count


if __name__ == '__main__':
    print(count_leaf_items(colours))
