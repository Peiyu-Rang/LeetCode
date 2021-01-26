# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        
        n = len(s)
        left = 0
        right = 0
        max_repeat = 0
        res = 0
        
        while right < n:
            if s[right] not in dic:
                dic[s[right]] = 0
            dic[s[right]] +=1
            max_repeat = max(max_repeat, dic[s[right]])
            
            win_len = right - left + 1
            while win_len - max_repeat > k:
                dic[s[left]] -=1
                left +=1
                
                win_len = right - left + 1
                
            res = max(res, win_len)
            
            right +=1
            
        
        return res
                