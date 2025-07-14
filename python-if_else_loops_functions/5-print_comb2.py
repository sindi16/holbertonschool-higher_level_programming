#!/usr/bin/python3

for i in range(0, 100):
    if i <= 9:
        i = "0" + str(i)
    if i != 99:
        print("{}".format(i), end=", ")
    else:
        print("{}".format(i))
