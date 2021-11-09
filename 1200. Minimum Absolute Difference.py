# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:27:47 2021

@author: Caven
"""


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        n = len(arr)
        min_diff = float('inf')
        res = []
        for i in range(n-1):
            diff = arr[i+1] - arr[i]
            if diff < min_diff:
                res = [[arr[i], arr[i+1]]]
                min_diff = diff
            elif diff == min_diff:
                res.append([arr[i], arr[i+1]])
        
        return res