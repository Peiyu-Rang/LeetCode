# -*- coding: utf-8 -*-
"""
Created on Sun May 16 14:06:14 2021

@author: Caven
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_dir = [0, 1, 0, -1]
        col_dir = [1, 0, -1, 0]
        
        seen = set()
        
        m = len(matrix)
        n = len(matrix[0])
        
        i = 0
        j = 0
        
        direction = 0
        
        res = []
        while len(seen) < m*n:
            if (i,j) not in seen and i < m and j < n:
                res.append(matrix[i][j])
                seen.add((i,j))
                if ((i == 0 and j == n-1) or (i == m-1 and j == n-1) or (i == m-1 and j == 0)) and not (i == 0 and j == 0):
                    direction +=1
                
            else:
                i -= row_dir[direction % 4]
                j -= col_dir[direction % 4]
                direction +=1
                
            i += row_dir[direction % 4]
            j += col_dir[direction % 4]
            
        return res
                
                    
                
                
        
        