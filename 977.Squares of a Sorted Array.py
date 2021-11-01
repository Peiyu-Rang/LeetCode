# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:37:16 2021

@author: Caven
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in nums:
            if i <= 0:
                neg.append(i)
            else:
                pos.append(i)
                
        neg = neg[::-1]
        n_pos = len(pos)
        n_neg = len(neg)
        
        p_pos = 0
        p_neg = 0
        
        res = []
        while p_pos < n_pos or p_neg < n_neg:
            if p_pos >= n_pos:
                res.append(neg[p_neg] ** 2)
                p_neg +=1
            elif p_neg >= n_neg:
                res.append(pos[p_pos] ** 2)
                p_pos +=1
            elif pos[p_pos] ** 2 >= neg[p_neg] ** 2:
                res.append(neg[p_neg] ** 2)
                p_neg +=1
            else:
                res.append(pos[p_pos] ** 2)
                p_pos +=1
                
        return res
    
    
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) -1
        
        res = []
        while left <= right:
            if nums[left]**2 <= nums[right]**2:
                res.append(nums[right]**2)
                right -=1
            else:
                res.append(nums[left]**2)
                left +=1
                
        return res[::-1]