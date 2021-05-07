# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:35:29 2021

@author: Caven
"""


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        
        for i in nums:
            if len(str(i)) % 2 == 0:
                count +=1
                
        return count