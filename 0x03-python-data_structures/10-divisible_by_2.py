#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divchecker = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            divchecker.append(True)
        else:
            divchecker.append(False)

    return (divchecker)
