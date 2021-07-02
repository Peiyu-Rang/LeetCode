# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 11:39:11 2020

@author: Caven
"""

import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        totalMove = m+n-2
        downMove = m-1
        return int(math.factorial(totalMove)/math.factorial(downMove)/math.factorial(n-1))
    
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        board = [[0]* n for i in range(m)]
        
        board[0][1:] = [1] * (n-1)
        for r in range(1,m):
            board[r][0] = 1
        
        for r in range(1,m):
            for c in range(1, n):
                board[r][c] = board[r-1][c] + board[r][c-1]
                
        return board[m-1][n-1]