# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 20:07:10 2018

@author: rpy
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0 or (x % 10 == 0 and x!=0)):
            return False
        revNum = 0
        while(x > revNum):
            revNum = 10 * revNum + x%10
            x = x//10
            
        return x == revNum or x == revNum //10