#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    x = len(sys.argv) - 1
    if x == 0:
        print("0 arguments.")
    elif x == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(x))
    for i in range(1, x + 1):
        print("{:d}: {:s}".format(i, sys.argv[i]))
