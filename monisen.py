# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 15:11:38 2016

@author: yangjun1
"""
import math

def isPrime(n):
    if n <= 2:
        return False
    for i in range(2, int(math.sqrt(n) ) ):
        if n % i == 0:
            return False
            
    return True
   
#寻找n个monisen数  
def getMonisen(n):
    result = []
    x = 3
    
    while(True):
        if( isPrime(x) and isPrime(2**x - 1)):
            result.append(2**x - 1)
            
        if(len(result) == n):
            break
            
        x += 2
            
    return result
    
print(getMonisen(5))
        