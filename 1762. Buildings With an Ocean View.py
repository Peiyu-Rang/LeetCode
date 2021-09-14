# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 16:51:30 2021

@author: Caven
"""


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = []
        max_height = -float('inf')
        
        for i in range(n-1, -1, -1):
            if heights[i] > max_height:
                res.append(i)
                max_height = heights[i]
        
        return res[::-1]
                
            