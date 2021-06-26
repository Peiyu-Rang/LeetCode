# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 18:44:58 2020

@author: Caven
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        j = 0
        
        max_len = 0
        
        seen = set()
        
        if n < 2:
            return n
        
        
        while j < n:
            if s[j] not in seen:
                seen.add(s[j])
                j +=1
                max_len = max(j - i, max_len)
            else:
                seen.remove(s[i])
                i += 1
        
        return max_len
    
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        n = len(s)
        left = 0
        right = 0
        max_len = 0
        
        if n < 2:
            return n
        
        while right < n:
            if s[right] not in seen:
                seen.add(s[right])
                right +=1
                max_len = max(right - left, max_len)
                
            else:
                seen.remove(s[left])
                left +=1
                
        return max_len