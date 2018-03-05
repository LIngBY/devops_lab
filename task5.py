#!/usr/bin/env python
'''Task5'''
# pylint: disable=invalid-name
company = input("Input company name: ")
i = 1
mydict = {company[0]: 1}
while i < len(company):
    if mydict.get(company[i]):
        mydict[company[i]] += 1
    else:
        mydict[company[i]] = 1
    i += 1
tempdict = sorted(mydict.items(), key=lambda item: (-item[1], item[0]))
for i in range(3):
    print(tempdict[i][0], tempdict[i][1])
