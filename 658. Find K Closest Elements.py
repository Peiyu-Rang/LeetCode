# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 21:18:35 2021

@author: Caven
"""


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        target = x - (k//2)
        
        n = len(arr)
        left = 0
        right = n - k
        
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid +1
            else:
                right = mid
                
        return arr[left: left + k]\