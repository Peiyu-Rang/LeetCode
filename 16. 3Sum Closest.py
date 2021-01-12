# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 16:05:23 2021

@author: Caven
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        
        for i in range(len(nums)):
            low = i +1
            high = len(nums)-1
            
            while(low < high):
                total = nums[i] + nums[low] + nums[high]
                if abs(target - total) < abs(diff):
                    diff = target - total
                if total < target:
                    low +=1
                elif total == target:
                    return target
                else:
                    high -=1
                
            
            if diff == 0:
                return target
                
        return target - diff