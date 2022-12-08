#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = 0
    key = ""
    if type(a_dictionary) != dict or len(a_dictionary) == 0:
        return None
    for k, v in a_dictionary.items():
        if v > biggest:
            biggest = v
            key = k
    return key
