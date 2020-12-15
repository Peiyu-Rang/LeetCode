# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 08:56:33 2020

@author: Caven
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n-1
        
        
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -=1
            elif numbers[left] + numbers[right] < target:
                left +=1
            else:
                return [left+1, right+1]