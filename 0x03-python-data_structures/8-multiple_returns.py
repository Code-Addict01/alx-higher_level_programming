#!/usr/bin/python3
def multiple_returns(sentence):
    sentlen = len(sentence)

    if (sentlen == 0):
        new_tuple = (sentlen, None)
    else:
        new_tuple = (sentlen, sentence[0])

    return new_tuple
