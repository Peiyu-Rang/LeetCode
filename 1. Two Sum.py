# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:32:10 2020

@author: Caven
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        n = len(nums)
        
        for i in range(n):
            if target - nums[i] in dic:
                return [i, dic[target - nums[i]]]
            else:
                dic[nums[i]] = i