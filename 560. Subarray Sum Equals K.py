# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 20:51:11 2021

@author: Caven
"""


from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        dic = defaultdict(int)
        dic[0] = 1
        
        n = len(nums)
        
        for i in range(n):
            total += nums[i]
            if (total - k) in dic:
                count += dic[total-k]
            dic[total] +=1
            
        return count