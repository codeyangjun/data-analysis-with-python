# -*- coding: utf-8 -*-
"""
Created on Tue May 03 10:43:06 2016

@author: yangjun1
"""
chars = ['a','b','c','d','e','f','g','h','i','j','k',\
'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#print chars
values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#print values
inputStr = raw_input()
inputStr = inputStr.lower()
for ch in inputStr:
    if ch in chars:
        index = chars.index(ch)
        values[index] += 1
        
print values
