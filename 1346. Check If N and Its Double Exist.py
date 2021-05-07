# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:25:42 2021

@author: Caven
"""


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        if counter[0] >=2:
            return True
        
        for item in arr:
            if item * 2 in arr and item != 0:
                return True
        
        return False