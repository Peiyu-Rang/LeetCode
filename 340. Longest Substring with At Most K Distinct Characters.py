# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 06:24:07 2021

@author: Caven
"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n*k == 0:
            return 0
        
        left = 0
        right = 0
        hashmap = {}
        
        maxLen = 1
        while right < n:
            hashmap[s[right]] = right
            right +=1
            
            if len(hashmap) == k+1:
                delIdx = min(hashmap.values())
                del hashmap[s[delIdx]]
                
                left = delIdx + 1
                
            maxLen = max(maxLen, right -left)
            
        return maxLen