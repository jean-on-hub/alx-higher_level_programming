#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = str(number)[-1]
if number < 0:
    ld = int(ld) * -1
    print(f"Last digit of {number:d} is {ld} and is less than 6 and not 0")
elif number == 0:
    print(f"Last digit of {number:d} is {number} and is {number}")
elif int(ld) > 5:
    print(f"Last digit of {number:d} is {ld} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {ld} and is less than 6 and not 0")
