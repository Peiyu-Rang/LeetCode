# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 15:39:44 2020

@author: Caven
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        
        f1 = nums[0]
        f2 = max(nums[:2])
        ans = [nums[0]]
        ans.append(f2)
        for i in range(2,n):
            ans.append(max(ans[-1], nums[i] + ans[-2]))
            
        return ans[-1]