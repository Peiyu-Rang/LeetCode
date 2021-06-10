# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 21:51:25 2021

@author: Caven
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        return self.backtrack(0, set(), set(), set(), n)
        
    def backtrack(self, row, diagonals, anti_diagonals, cols, n):
        if row == n:
            return 1
        solution = 0
        
        for col in range(n):
            curr_diagonal = row - col
            curr_anti_diagonal = row + col
            
            if (col in cols) or curr_diagonal in diagonals or curr_anti_diagonal in anti_diagonals:
                continue
            
            cols.add(col)
            diagonals.add(curr_diagonal)
            anti_diagonals.add(curr_anti_diagonal)
            
            solution += self.backtrack(row+1, diagonals, anti_diagonals, cols,n)
            
            cols.remove(col)
            diagonals.remove(curr_diagonal)
            anti_diagonals.remove(curr_anti_diagonal)
            
        return solution