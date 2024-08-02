#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    dict_keys = list(a_dictionary.keys())

    for i in dict_keys:
        count += 1

    return (count)
