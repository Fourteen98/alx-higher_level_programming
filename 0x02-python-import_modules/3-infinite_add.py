#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    answer = 0
    for x in sys.argv:
        if x != sys.argv[0]:
            answer += int(x)
    print(answer)
