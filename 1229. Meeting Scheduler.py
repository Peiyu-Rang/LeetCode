# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:22:57 2021

@author: Caven
"""

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        n1 = len(slots1)
        n2 = len(slots2)
        
        i = 0
        j = 0
        
        slots1.sort()
        slots2.sort()
        
        while i < n1 and j < n2:
            start1, end1 = slots1[i]
            start2, end2 = slots2[j]
            
            if start1 <= start2:
                meeting_start = start2
            else:
                meeting_start = start1
                
            if end1 <= end2:
                meeting_end = end1
            else:
                meeting_end = end2
            
            if meeting_end - meeting_start >= duration:
                return [meeting_start, meeting_start + duration]
            else:
                if end1 < end2:
                    i +=1
                else:
                    j +=1
                    
            
        return []
        