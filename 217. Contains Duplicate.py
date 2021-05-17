# -*- coding: utf-8 -*-
"""
Created on Sun May 16 20:18:47 2021

@author: Caven
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for item in nums:
            if item in seen:
                return True
            else:
                seen.add(item)
                
        return False
        