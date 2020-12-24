# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 22:44:00 2020

@author: Caven
"""


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        nrow = len(board)
        ncol = len(board[0])
        
        state = [[0] * ncol for i in range(nrow)]
        
        # update state
        stable = True
        for i in range(nrow):
            for j in range(ncol-2):
                if board[i][j] == board[i][j + 1] == board[i][j+2] != 0:
                    state[i][j] = state[i][j+1] = state[i][j+2] = 1
                    stable = False
        for j in range(ncol):
            for i in range(nrow-2):
                if board[i][j] == board[i+1][j] == board[i+2][j] != 0:
                    state[i][j] = state[i+1][j] = state[i + 2][j] = 1
                    stable = False
        
        if stable:
            return board
        
        # update the board
        for j in range(ncol):
            offset = 0
            for i in range(nrow, -1, -1):
                k = i + offset
                if k < nrow:
                    if state[i][j] == 1:
                        offset +=1
                    else:
                        board[k][j] = board[i][j]
            for i in range(offset):
                board[i][j] = 0
        
        return self.candyCrush(board)