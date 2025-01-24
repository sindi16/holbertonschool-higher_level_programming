#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    nr_elem = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                nr_elem += 1
            else:
                continue
        except IndexError:
            raise IndexError
            break
    print()
    return nr_elem
    