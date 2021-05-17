# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:06:10 2020

@author: Caven
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        
        i,j = 0,0
        total = nums[0]
        min_len = None
        
        while j < n and i < n:
            if total < target:
                if j < n-1:
                    j +=1
                    total += nums[j]
                else:
                    break
            else:
                if not min_len:
                    min_len = j - i + 1
                else:
                    if j - i +1 < min_len:
                        min_len = j - i + 1
                    else:
                        total -= nums[i]
                        i +=1
                
                
        return min_len if min_len else 0
        
        
        
