#!/usr/bin/python3
def multiple_returns(sentence):
    # multiple_returns - returns tuple with length of a string and its 1st char

    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
