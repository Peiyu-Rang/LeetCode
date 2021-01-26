# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:33:57 2021

@author: Caven
"""

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        
        l = 0
        r = 0
        
        count_dict = {1:0, 0:0}
        
        max_1_count = 0
        res = 0
        
        while r < n:
            count_dict[A[r]] += 1
            
            max_1_count = max(max_1_count, count_dict[1])
            
            win_len = r - l + 1
            
            while win_len - max_1_count > K:
                count_dict[A[l]] -=1
                l +=1
                
                win_len = r - l + 1
            
            res = max(res, win_len)
            r +=1
            
        return res
                
