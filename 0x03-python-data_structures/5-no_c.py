#!/usr/bin/python3
def no_c(my_string):
    # no_c - function that removes all characters c and C from a string

    new_string = ""
    for x in range(len(my_string)):
        if my_string[x] != "c" and my_string[x] != "C":
            new_string += my_string[x]
    return (new_string)