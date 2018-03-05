#!/usr/bin/python
'''Task3 programm'''
# pylint: disable=invalid-name
x = int(input("Input X: "))
y = int(input("Input Y: "))
print(x)
print(y)
print(bin(x ^ y)[2:])
print(len(bin(x ^ y)[2:]))
print((bin(x ^ y)[2:]).count('1'))
