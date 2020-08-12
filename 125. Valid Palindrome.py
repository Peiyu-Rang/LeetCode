# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:36:47 2020

@author: Caven
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace('.', '')
        s = s.replace(' ', '')
        s = s.replace(',', '')
        n = len(s)
        i = 0
        j = n-1
        if n < 2:
            return True
        while(i < j):
            while(not s[i].isalnum() and i < n-1):
                i +=1
            while(not s[j].isalnum() and j > 0):
                j -=1
            
            if s[i].lower() == s[j].lower():
                i+=1
                j-=1
            else:
                return False
            
        return True