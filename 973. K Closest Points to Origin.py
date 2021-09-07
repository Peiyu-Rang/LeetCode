# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 17:32:40 2021

@author: Caven
"""


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mappings = collections.defaultdict(list)
        
        for cord in points:
            dist = math.sqrt(cord[0]**2 + cord[1]**2)
            mappings[dist].append(cord)
        
        mappings_sorted = {key: mappings[key] for key in sorted(mappings.keys())}
        
        res = []
        
        for key in mappings_sorted:
            if mappings_sorted[key]:
                for item in mappings_sorted[key]:
                    if k > 0:
                        res.append(item)
                        k -=1
                
        return res
        