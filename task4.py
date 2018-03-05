#!/usr/bin/env python
'''Task4'''
# pylint: disable=invalid-name
import re
N = int(input("Input N: "))
print(N)
i = 0
mylist = []
while i < N:
    mylist.append(input("Input string: "))
    i += 1
result = -1
flag = 0
temp = 0
for x in range(N):
    if int(mylist[x][-1]) == 1:
        if flag == 0:
            temp = int(re.search(r'\d+', mylist[x]).group())
            result = x + 1
            flag = 1
        if temp < int(re.search(r'\d+', mylist[x]).group()):
            temp = int(re.search(r'\d+', mylist[x]).group())
            result = x + 1
print(result)
