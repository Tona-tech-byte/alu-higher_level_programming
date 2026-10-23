#!/usr/bin/python3
def uppercase(str):
    result = "{}".format(str)
    output = ""
    for char in result:
        if ord('a') <= ord(char) <= ord('z'):
            output += chr(ord(char) - 32)
        else:
            output += char
    print("{:s}".format(output))
