# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:54:06 2021

@author: Caven
"""


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        mono_queue = []
        n = len(nums)
        left = n
        right = 0
        
        for i in range(n):
            while mono_queue and nums[mono_queue[-1]] > nums[i]:
                left = min(left, mono_queue.pop())
                
            mono_queue.append(i)
            
        mono_queue = []
        
        for i in range(n-1, -1, -1):
            while mono_queue and nums[mono_queue[-1]] < nums[i]:
                right = max(right, mono_queue.pop())
                
            mono_queue.append(i)
            
        return right - left + 1 if right > left else 0
            