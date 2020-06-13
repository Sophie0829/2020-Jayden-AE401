# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:28:04 2020

@author: jaych
"""


d={}

while True:  
     
    key=input("請輸入單字(按0跳出):")
    
    
    if key == str(0):    
        print(d)        
        break
    else:
        
        if key not in d.keys():
            value=input("請輸入翻譯：")
            d[key]=value
        else: 
            print("此單字已在字典中，請輸入其他單字！")
