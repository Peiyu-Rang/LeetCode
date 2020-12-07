# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 22:21:25 2020

@author: Caven
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n == 1:
            return 0
        if n == 2:
            return min(height)
        left = 0
        right = n-1
        maxArea = 0
        while left < right:
            if min(height[left], height[right]) * (right - left) > maxArea:
                maxArea  = min(height[left], height[right]) * (right - left)
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        
        return maxArea