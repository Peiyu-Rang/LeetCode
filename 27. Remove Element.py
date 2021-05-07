# -*- coding: utf-8 -*-
"""
Created on Thu May  6 18:07:34 2021

@author: Caven
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[j] != val:
                nums[i] = nums[j]
                i +=1
                
        return i