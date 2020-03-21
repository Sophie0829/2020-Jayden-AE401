# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 12:13:32 2020

@author: jaych
"""


score=input("請輸入你的成績:")
score=int(score)
if score>=90:
        print("A")
elif score<90 and score>80:
        print("B")
elif score<80 and score>70:
       print("C")


else :
        print("D")