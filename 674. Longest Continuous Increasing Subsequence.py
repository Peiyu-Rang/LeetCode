# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 23:00:52 2021

@author: Caven
"""


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 0
        curr_len = 0
        left = 0
        right = 0
        n = len(nums)
        
        while right < n:
            if left == right or nums[right] > nums[right - 1]:
                right +=1
            else:
                curr_len = right - left
                res = max(res, curr_len)
                left = right
                right +=1
                
        curr_len = right - left
        res = max(res, curr_len)
        return res