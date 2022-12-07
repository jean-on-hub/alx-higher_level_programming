#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if 122 >= ord(ch) >= 97:
            ch = chr(ord(ch) - 32)
        print("{}".format(ch), end="")
    print("")
