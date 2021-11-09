# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 15:26:43 2021

@author: Caven
"""


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        id_time = collections.defaultdict(set)
        
        for i, t in logs:
            id_time[i].add(t)
            
        id_time_count = {key: len(id_time[key]) for key in id_time}
        
        res = [0] * k
        
        for key in id_time_count:
            res[id_time_count[key] -1] +=1
            
        return res