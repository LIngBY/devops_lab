#!/usr/bin/python
'''Task3 programm'''
# pylint: disable=invalid-name
x = int(input("Input X: "))
y = int(input("Input Y: "))
print((bin(x ^ y)[2:]).count('1'))
