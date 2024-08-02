#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dict = list(a_dictionary.keys())
    sort_dict.sort()
    for i in sort_dict:
        print("{}: {}".format(i, a_dictionary.get(i)))
