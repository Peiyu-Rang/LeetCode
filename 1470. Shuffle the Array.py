# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:40:52 2020

@author: Caven
"""


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
            
        return ans
        