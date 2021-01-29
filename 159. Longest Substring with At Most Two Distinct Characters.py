# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 21:28:43 2021

@author: Caven
"""

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        dic = {}
        
        i = 0
        j = 0
        
        res = 0
        
        
        n = len(s)
        if n < 3:
            return n
        
        while j < n:
            dic[s[j]] = j
            j +=1
            
            if len(dic) == 3:
                del_idx = min(dic.values())
                del dic[s[del_idx]]
                
                i = del_idx + 1
                
            res = max(res, j - i)
            
        return res
        
            
