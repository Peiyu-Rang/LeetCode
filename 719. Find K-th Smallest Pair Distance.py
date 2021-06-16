# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 07:44:37 2021

@author: Caven
"""


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def possible(guess): # if the number of pairs with distance <= guess is larger or equal than k
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left +=1
                    
                count += right - left
            return count >= k
        
        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) // 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1
                
        return lo