# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 15:43:48 2020

@author: Caven
"""


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1 = min(nums)
        max2 = min(nums)
        max3 = min(nums)
        min1 = max(nums)
        min2 = max(nums)
        for n in nums:
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n

            elif n <= max1 and n > max2:
                max3 = max2
                max2 = n
            elif n <= max2 and n > max3:
                max3 = n

            if n < min2:
                min1 = min2
                min2 = n
            elif n >= min2 and n < min1:
                min1 = n
        
        return max(max1 * max2 * max3, max1 * min1 * min2)