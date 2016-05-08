# -*- coding: utf-8 -*-
"""
Created on Sun May 08 19:53:37 2016

@author: yangjun1
"""
names = ["xiaoyun","xiaohong","xiaoteng","xiaoyi","xiaoyang"]
QQs = [88888,5555555,11111,1234321,1212121]

dic = dict(zip(names,QQs))
name = raw_input("Please input the name:")
#print name
while(True):
    if(name in dic.keys()):
        print name + '\'s QQ is:' + str(dic[name])
        break;
    else:
        name = raw_input("Please input the name again:")

print  "Who has the nice QQ number?"        
for name in dic.keys():
    if(dic[name] < 100000):
        print name + ': ' + str(dic[name])