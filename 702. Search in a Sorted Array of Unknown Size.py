# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 22:02:51 2021

@author: Caven
"""


# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        
        if reader.get(0) == target:
            return 0
        
        left = 0
        right = 1
        
        # get the boundary
        while reader.get(right) < target:
            left = right
            right *=2
            
        # binary search
        while left <= right:
            mid = (left + right) // 2
            num = reader.get(mid)
            
            if num == target:
                return mid
            elif num > target:
                right = mid -1
            else:
                left = mid + 1
                
        return -1
        