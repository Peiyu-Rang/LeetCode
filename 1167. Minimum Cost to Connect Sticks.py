# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 21:06:31 2021

@author: Caven
"""


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        res = 0
        
        heapq.heapify(sticks)
        
        while len(sticks) > 1:
            s1 = heapq.heappop(sticks)
            s2 = heapq.heappop(sticks)
            
            res += s1 + s2
            
            heapq.heappush(sticks, s1+s2)
            
        return res