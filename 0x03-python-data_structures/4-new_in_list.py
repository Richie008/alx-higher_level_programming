#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list

original_list = [1, 2, 3, 4]
modified_list = new_in_list(original_list, 2, 10)
print(original_list)  # [1, 2, 3, 4]
print(modified_list)  # [1, 2, 10, 4]

