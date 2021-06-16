# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 08:21:05 2021

@author: Caven
"""


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        res = -1
        lo, hi = min(nums), sum(nums)
        
        while lo <= hi:
            mi = (lo + hi)//2
            if self.can_split(nums, m, mi):
                res = mi
                hi = mi - 1
            else:
                lo = mi + 1
                
        return res
    
    def can_split(self,nums, m, mi):
        if max(nums) > mi:
            return False
        
        count = 1
        curr_sum = 0
        i = 0
        while i < len(nums):
            if curr_sum + nums[i] > mi:
                count +=1
                curr_sum = 0
                
            curr_sum += nums[i]
            i +=1
            
        return count <= m