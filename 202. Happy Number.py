# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 14:44:29 2020

@author: Caven
"""

class Solution:
    def isHappy(self, n:int) -> bool:
        maxIter = 100
        count = 0
        def help(n)：:
            nStr = str(n)
            sumSq = 0
            for l in nStr:
                sumSq += int(l)*int(l)
            return sumSq
        
        while(count < maxIter):
            n = help(n)
            if int(n) ==1:
                return True
            count +=1
        
        return False