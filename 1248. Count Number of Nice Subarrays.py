# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 15:03:13 2021

@author: Caven
"""


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [num %2 for num in nums]
        def subStringAtMostOdd(k):
            counter = collections.defaultdict(int)
            left = 0
            res = 0
            
            for right, num in enumerate(nums):
                counter[num] +=1
                while counter[1] > k:
                    counter[nums[left]] -=1
                
                    left +=1
            
                res += right - left + 1
            
            return res
        
        return subStringAtMostOdd(k) - subStringAtMostOdd(k-1)
                