# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:23:11 2020

@author: jaych
"""
studentname=[]

scores=[]

num=int(input("請輸入學生人數:"))

for i in range(num):
    
    name=input("請輸入學生姓名:")
    studentname.append(name)
    x=int(input("輸入分數:"))
    scores.append(x)  


print(scores)

###############################################################################

sum=0
for i in range(num):
    sum=sum+scores[i]

avg=sum/num
print("平均分數",avg)
###############################################################################
highest=0
lowest=100
for i in range(num):
     
    if scores[i]>highest:
        highest=scores[i]
        h=i
    if scores[i]<lowest:
        lowest=scores[i]
        l=i
print("最高分；",highest,"是:",studentname[h])
print("最低分；",lowest,"是:",studentname[l])
