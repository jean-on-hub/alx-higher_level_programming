#!/usr/bin/python3
for ch in range(ord("a"), ord("z") + 1):
    if chr(ch) == "q" or chr(ch) == "e":
        continue
    print("{:c}".format(ch), end="")
