# -*- coding: utf-8 -*-
"""
Created on Thu May  6 21:48:26 2021

@author: Caven
"""


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expect = sorted(heights)
        n = len(heights)
        count = 0
        for i in range(n):
            if expect[i] != heights[i]:
                count +=1
                
        return count