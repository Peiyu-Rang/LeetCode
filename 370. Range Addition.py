# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 21:13:56 2021

@author: Caven
"""


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * length
        for start, end, inc in updates:
            res[start] += inc
            if end + 1 < length:
                res[end+1] -= inc
            
        total = 0
        final_ans = []
        
        for i in res:
            total += i
            final_ans.append(total)
            
        return final_ans