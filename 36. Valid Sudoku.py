# -*- coding: utf-8 -*-
"""
Created on Mon May  3 23:08:24 2021

@author: Caven
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = {}
        seen_col = {}
        seen_pal = {}
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if i in seen_row:
                    if board[i][j] in seen_row[i]:
                        return False
                    else:
                        seen_row[i].append(board[i][j])
                else:
                    seen_row[i] = [board[i][j]]
                    
                if j in seen_col:
                    if board[i][j] in seen_col[j]:
                        return False
                    else:
                        seen_col[j].append(board[i][j])
                else:
                    seen_col[j] = [board[i][j]]
                    
                if (i // 3 * 10 + j // 3) in seen_pal:
                    if board[i][j] in seen_pal[i // 3 * 10 + j // 3]:
                        return False
                    else:
                        seen_pal[i // 3 * 10 + j // 3].append(board[i][j])
                else:
                    seen_pal[i // 3 * 10 + j // 3] = [board[i][j]]
                    
                
        return True