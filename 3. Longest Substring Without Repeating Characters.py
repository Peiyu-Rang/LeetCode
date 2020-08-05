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
        ans = 0
        seen = set()
        while(j < n):
            if s[j] in seen:
                seen.remove(s[i])
                i +=1
            else:
                seen.add(s[j])
                j +=1
                ans = max(ans, j-i)
        
        return ans