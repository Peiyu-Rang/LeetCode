# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 08:07:28 2021

@author: Caven
"""

# merge sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <2:
            return nums
        
        mid = n // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        return self.merge(left, right)
    
    def merge(self, left, right):
        nl = len(left)
        nr = len(right)
        
        lp = 0
        rp = 0
        res = []
        while lp < nl and rp < nr:
            if left[lp] < right[rp]:
                res.append(left[lp])
                lp +=1
            else:
                res.append(right[rp])
                rp +=1
                
        res += left[lp:]
        res += right[rp:]
        
        return res
                