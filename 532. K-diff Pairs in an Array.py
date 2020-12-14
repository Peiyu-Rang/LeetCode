# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 10:03:09 2020

@author: Caven
"""

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import Counter
        
        hash_nums = Counter(nums)
        ans = 0
        
        if k != 0:
            for key in hash_nums:
                if key+k in hash_nums:
                    ans +=1
        else:
            for key in hash_nums:
                if hash_nums[key] > 1:
                    ans += 1
                
        return ans