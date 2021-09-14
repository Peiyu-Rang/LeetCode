# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 16:13:05 2021

@author: Caven
"""


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []
        
        for log in logs:
            f_id, state, timestamp = log.split(":")
            f_id, timestamp = int(f_id), int(timestamp)
            
            if stack:
                result[stack[-1]] += timestamp - previous_timestamp
            
            if state == "start":
                stack.append(f_id)
            else:
                ## need to +1 since function ends at the end of unit time
                result[stack.pop()] += 1
                timestamp += 1

            previous_timestamp = timestamp
        
        return result