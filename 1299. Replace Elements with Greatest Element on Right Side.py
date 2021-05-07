# -*- coding: utf-8 -*-
"""
Created on Thu May  6 21:27:48 2021

@author: Caven
"""


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = -1
        n = len(arr)
        i = n-1
        while i >= 0:
            temp = arr[i]
            arr[i] = maxi
            maxi = max(temp, maxi)
            i -=1
            
        return arr