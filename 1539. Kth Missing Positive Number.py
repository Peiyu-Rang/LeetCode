# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:05:03 2021

@author: Caven
"""


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr)-1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] - mid -1 < k:
                left = mid + 1
            else:
                right = mid -1
                
        return left + k