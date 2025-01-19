#!/usr/bin/python3
for i in range(10):
    for x in range(0,10):
        if i == 8 and x == 9:
            print('{}{}'.format(i, x), end="\n")
        elif i < x:
            print('{}{}'.format(i, x), end=", ")
        