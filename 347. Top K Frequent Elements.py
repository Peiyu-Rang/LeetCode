# -*- coding: utf-8 -*-
"""
Created on Mon May 17 18:33:48 2021

@author: Caven
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        counter_desc = {k: v for k, v in sorted(counter.items(), key=lambda item: item[1], reverse = True)}
        
        res = []
        for i,v in enumerate(counter_desc):
            if i < k:
                res.append(v)
            else:
                break
                
        return res