# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 23:04:59 2021

@author: Caven
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        idx = 0
        word_len = len(word)
        
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