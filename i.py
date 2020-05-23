# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:56:42 2020

@author: jaych
"""


scores=[]

num=int(input("人數:"))

for i in range(num):
    
    x=int(input("分數:"))
    scores.append(x)

print(scores)

##############################################################################

highest=max(scores)
lowest=min(scores)
average=sum(scores)/num


print("最高:",highest)
print("最低:",lowest)
print("平均:",average)



