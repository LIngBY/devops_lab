#!/usr/bin/env python
'''Task1'''
# pylint: disable=invalid-name
N = int(input("Input N: "))
print(N)
i = 0
mylist = []
while i < N:
    inpSTR = input("Input command: ")
    if inpSTR.split(' ')[0] == 'insert':
        mylist.insert(int(inpSTR.split(' ')[1]), int(inpSTR.split(' ')[2]))
    elif inpSTR.split(' ')[0] == 'print':
        print(mylist)
    elif inpSTR.split(' ')[0] == 'remove':
        mylist.remove(int(inpSTR.split(' ')[1]))
    elif inpSTR.split(' ')[0] == 'append':
        mylist.append(int(inpSTR.split(' ')[1]))
    elif inpSTR.split(' ')[0] == 'sort':
        mylist.sort()
    elif inpSTR.split(' ')[0] == 'pop':
        mylist.pop()
    elif inpSTR.split(' ')[0] == 'reverse':
        mylist.reverse()
    i += 1
