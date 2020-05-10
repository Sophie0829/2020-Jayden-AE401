# -*- coding: utf-8 -*-
"""
Created on Sun May 10 19:18:20 2020

@author: jaych
"""
music=list()

num=input("全班人數:")
num=int(num)

for i in range(num):
    name=input("學生名稱:")
    scores=input("音樂成績:")
    scores=int(scores)
    
    
    student=list()
    student.append(name)
    student.append(scores)
   
   
    music.append(student)

print("音樂成績；",music)

sum=0

for i in music:
    sum=sum+i[1]
    
avg=sum/num
print("平均分數=",avg)

highest=0

for i in music:
    if i[1]>highest:
        highest=i[1]
        higheststudent=i[0]
        
print("最高分是",higheststudent,highest,"分")



lowest=100
for i in music:
    if i[1]<lowest:
        lowest=i[1]
        loweststudent=i[0]
print("最低分是",loweststudent,lowest,"分")










































