#!/usr/bin/python3
def weight_average(my_list=[]):

    if len(my_list) == 0:
        return 0

    add = 0
    div = 0
    for k in my_list:
        add += k[0] * k[1]
        div += k[1]
    return add/div
