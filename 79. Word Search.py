# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 23:04:59 2021

@author: Caven
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        def backtrack(i,j,word):
            if len(word) == 0:
                return True
            if i < 0 or j < 0 or i >= m or j>=n:
                return False
            
            if board[i][j] == word[0]:
                board[i][j] = '0'
                res = backtrack(i-1,j, word[1:]) or backtrack(i+1,j, word[1:]) or backtrack(i,j-1, word[1:]) or backtrack(i,j+1, word[1:])
                board[i][j] = word[0]
                return res
        
        
        for i in range(m):
            for j in range(n):
                if backtrack(i,j, word):
                    return True
        return False
    
    
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        l = len(word)
        
        if not word: return True
        if not board: return False
        
        
        def backtrack(i, j, idx, board):
            letter = board[i][j]
            if letter != word[idx]:
                return False
            elif idx == l-1:
                return True
            else:
                board[i][j] = '$'
                
                res = False
                for new_i, new_j in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                    if 0 <= new_i < m and 0 <= new_j < n:
                        if backtrack(new_i, new_j, idx+1, board):
                            return True
                
                board[i][j] = letter
                return False
            
           
        
        
        for i in range(m):
            for j in range(n):
                if backtrack(i,j,0, board):
                    return True
        
        return False