# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:53:54 2021

@author: Caven
"""


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zero_count = 0
        for i in arr:
            if i == 0:
                zero_count +=1
        
        for i in range(zero_count):
            arr.append(0)
                
        j = n + zero_count - 1
        
        for i in range(n-1, -1, -1):
            if arr[i] == 0:
                arr[j] = 0
                arr[j-1] = 0
                j -= 2
            else:
                arr[j] = arr[i]
                j -= 1
                
        for i in range(zero_count):
            arr.pop()