# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 16:46:40 2021

@author: Caven
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        n = len(heights)
        
        for i in range(n):
            while stack[-1] !=  -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            stack.append(i)
            
        
        while stack[-1]!= -1:
            current_height = heights[stack.pop()]
            current_width = n - stack[-1] -1
            max_area = max(max_area, current_height * current_width)
            
        return max_area