# -*- coding: utf-8 -*-
"""
Created on Mon May  3 23:08:24 2021

@author: Caven
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            seen = ['1','2','3','4','5','6','7','8','9']
            for item in row:
                if item in seen:
                    seen.pop(seen.index(item))
                elif item == '.':
                    continue
                else:
                    return False
        
        # check cols:
        for col in range(9):
            seen = ['1','2','3','4','5','6','7','8','9']
            for row in range(9):
                if board[row][col] in seen:
                    seen.pop(seen.index(board[row][col]))
                elif board[row][col] == '.':
                    continue
                else:
                    return False
                
        # check subunit
        
        for I in range(3):
            for J in range(3):
                seen = ['1','2','3','4','5','6','7','8','9']
                for i in range(3*I, 3*I + 3):
                    for j in range(3*J, 3*J + 3):
                        if board[i][j] in seen:
                            seen.pop(seen.index(board[i][j]))
                        elif board[i][j] == '.':
                            continue
                        else:
                            return False
                        
        return True