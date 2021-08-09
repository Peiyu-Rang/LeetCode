# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 23:24:20 2021

@author: Caven
"""


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        intervals = sorted(intervals, key = lambda x: x[0])
        
        for i in range(1,n):
            if intervals[i][0] < intervals[i-1][1]:
                return False
            
        return True