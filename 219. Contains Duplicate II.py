# -*- coding: utf-8 -*-
"""
Created on Sun May 16 21:33:30 2021

@author: Caven
"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i,v in enumerate(nums):
            if v in dic:
                if abs(i - dic[v]) <= k:
                    return True
                else:
                    dic[v] = i
            else:
                dic[v] = i
                
        return False