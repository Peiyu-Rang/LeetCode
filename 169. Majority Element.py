# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:22:52 2020

@author: Caven
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        dic = {}
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num] = 1
        
        for key in dic:
            if dic[key] > n/2:
                return key
            
            
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if candidate == num else -1)
            
        return candidate