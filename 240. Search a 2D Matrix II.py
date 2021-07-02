# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 08:30:29 2021

@author: Caven
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        row = m-1
        col = 0
        
        while row < m and col < n and row >=0 and col >=0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col +=1
            else:
                row -=1
        
        return False
        
    
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        i = m-1
        j = 0
        
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -=1
            else:
                j +=1
                
        return False