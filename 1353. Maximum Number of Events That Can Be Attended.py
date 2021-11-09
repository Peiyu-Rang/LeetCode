# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:56:28 2021

@author: Caven
"""


import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events)
        total_days = max([end for _, end in events])
        res = 0
        event_id = 0
        min_heap = []
        n = len(events)
        
        for day in range(1, total_days + 1):
            while event_id < n and events[event_id][0] == day:
                heapq.heappush(min_heap, events[event_id][1])
                event_id +=1
            
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
                
            if min_heap:
                heapq.heappop(min_heap)
                res +=1
        
        return res