#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keylist = list(a_dictionary)
    return ({x: a_dictionary[x]*2 for x in keylist})
