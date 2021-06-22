# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 16:46:16 2020

@author: Caven
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = nums[0]
        
        for i in range(1,n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            maxSum = max(nums[i], maxSum)
            
        return maxSum
    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]
        
        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
            
        return max_sum