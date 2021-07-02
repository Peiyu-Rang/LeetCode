# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 22:13:52 2021

@author: Caven
"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        used_rooms = 0
        
        start_meetings = sorted([i[0] for i in intervals])
        end_meetings = sorted([i[1] for i in intervals])
        
        n = len(intervals)
        
        end_pointer = 0
        start_pointer = 0
        
        while start_pointer < n:
            if start_meetings[start_pointer] >= end_meetings[end_pointer]:
                used_rooms -=1
                end_pointer +=1
                
            used_rooms +=1
            start_pointer +=1
            
        return used_rooms