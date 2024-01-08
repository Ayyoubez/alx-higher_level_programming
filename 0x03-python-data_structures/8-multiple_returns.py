#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_1 = ("None",)
    if len(sentence) == 0:
        return tuple_1[0]
    else:
        return (len(sentence)), sentence[0]
