# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:38:49 2020

@author: jaych
"""



import random

nameList=["Fifi", "Elim", "Jane"]
verbList=["正在踢", "正在打", "正在玩"]
nounList=["足球","球","皮球"]

def random_word(list):
    
    word = random.sample(list,1)
    
    return word[0]
    
def generateSentence(list1,list2,list3):
    
    sentence = random_word(list1) + random_word(list2)+ random_word(list3)
    
    return sentence 

for i in range(2):
    
    print(generateSentence(nameList,verbList,nounList))