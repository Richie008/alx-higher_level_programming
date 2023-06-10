#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list

original_list = [1, 2, 3, 4]
modified_list = replace_in_list(original_list, 2, 10)
print(modified_list)

