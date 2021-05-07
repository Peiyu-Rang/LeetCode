# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:36:56 2021

@author: Caven
"""


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3: 
            return False
        
        if arr[0] >= arr[1]:
            return False
        
        past_peak = False
        i = 1
        while i < n:
            if not past_peak:
                if arr[i] > arr[i-1]:
                    i +=1
                elif arr[i] == arr[i -1]:
                    return False
                else:
                    past_peak = True
                    i += 1
            else:
                if arr[i] >= arr[i - 1]:
                    return False
                else:
                    i +=1
        
        if past_peak:
            return True
        else:
            return False
        