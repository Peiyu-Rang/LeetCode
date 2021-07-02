# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 23:05:33 2021

@author: Caven
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        n = len(intervals)
        if n == 1:
            return intervals
        
        res = []
        curr_intv = intervals[0]
        
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
                
        return res