# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 10:45:47 2020

@author: jaych
"""


chars = []

myString = "I Love YOU"

###

for f in range (len(myString)):
    
    chars.append(ord(myString[f]))

print(chars)

###

for j in chars:
    
    print(chr(j+2),end = '')