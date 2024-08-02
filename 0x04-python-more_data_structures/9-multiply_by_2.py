#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    newdict_keys = list(new_dict.keys())

    for i in newdict_keys:
        new_dict[i] *= 2

    return (new_dict)
