# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:04:43 2021

@author: Caven
"""

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        i = 0
        res = 0
        
        while i < n:
            base = i
            
            # walk up
            while i + 1 < n and arr[i] < arr[i + 1]:
                i +=1
            
            # check if peak is valid
            if i == base:
                i +=1
                continue
            peak = i
            
            # walk down
            while i + 1 < n and arr[i] > arr[i + 1]:
                i +=1
            
            # check if end is valid
            if i == peak:
                i +=1
                continue 
            
            res = max(res, i - base + 1)
            
        return res