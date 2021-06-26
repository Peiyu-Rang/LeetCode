# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 18:37:59 2021

@author: Caven
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])
        row_set = set()
        col_set = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
                    
        for i in row_set:
            for j in range(n):
                matrix[i][j] = 0
        
        for j in col_set:
            for i in range(m):
                matrix[i][j] = 0