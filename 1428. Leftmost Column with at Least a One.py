# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:36:59 2021

@author: Caven
"""


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, col = binaryMatrix.dimensions()
        
        i = 0
        j = col - 1
        left_most = float('inf')
        
        while i < row:
            if binaryMatrix.get(i,j):
                mid = self.binarySearch(i, j, binaryMatrix)
                if mid != -1:
                    left_most = min(left_most, mid)
                    j = mid 
                
            i +=1
            
        return left_most if left_most < float('inf') else -1
                
    def binarySearch(self, row, idx, binaryMatrix):
        left = 0
        right = idx
        while left < right:
            mid = (left + right) // 2

            if binaryMatrix.get(row, mid) and (mid == 0 or not binaryMatrix.get(row, mid-1)):
                return mid
            elif binaryMatrix.get(row, mid):
                right = mid - 1
            else:
                left = mid + 1
                
        if binaryMatrix.get(row, left):
            return left
        else:
            return -1
            