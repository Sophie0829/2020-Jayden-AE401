# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 19:34:42 2020

@author: jaych
"""
score=input("請輸入你的英文成績:")
integer=input("請輸入你的數學成績:")
score=int(score)
if score>=90 and integer>=90:
        print("Excellent!")
elif score<60 and integer<60 :
        print("成績很爛喔~再加油")
elif score<60 or score<60:
       print("請繼續加油")
else :print("真可惜~差一點就滿分了")
