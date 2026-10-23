#!/usr/bin/python3
def uppercase(str):
    output = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            output += chr(ord(char) - 32)
        else:
            output += char
    print("{:s}".format(output))
