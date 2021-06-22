# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:36:47 2020

@author: Caven
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n-1
        while left < right:
            while(left < right and not s[left].isalnum()):
                left +=1
            while(left < right and not s[right].isalnum()):
                right -=1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left +=1
            right -=1
        
        return True
    
    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_s = []
        for ss in s:
            if ss.isalpha() or ss.isnumeric():
                valid_s.append(ss.lower())
                
        left, right = 0, len(valid_s)-1
        while left < right:
            if valid_s[left] != valid_s[right]:
                return False
            left +=1
            right -=1
        return True