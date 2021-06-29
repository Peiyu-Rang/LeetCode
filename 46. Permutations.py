# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 10:07:35 2021

@author: Caven
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def backtrack(first = 0):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                
                backtrack(first +1)
                
                nums[first], nums[i] = nums[i], nums[first]
            
        res = []
        backtrack()
        
        return res
    
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        if not nums:
            return res
        
        def backtrack(first = 0):
            if first == n-1:
                res.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
                
        backtrack()
        
        return res