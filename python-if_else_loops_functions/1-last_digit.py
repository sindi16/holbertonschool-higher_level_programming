#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
print(number)

ld = number%10
if ld > number:
    print(f"Last digit of {number} is {ld} and is greater than 5")
elif ld == 0:
    print("Last digit of {number} is {ld} and is less than 6")
else:
    print(f"Last digit of {number} is {ld} is 0 and is 0")

print()