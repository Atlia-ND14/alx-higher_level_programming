#!/usr/bin/python3
def uppercase(input_str):
    result = ""
    for char in input_str:
        result += chr(ord(char) - 32)
    print(result)
