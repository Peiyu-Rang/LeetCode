# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 22:35:29 2021

@author: Caven
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def could_place(d, row, col):
            return not (d in rows[row] or d in cols[col] or d in boxes[box_idx(row, col)])
        
        def place_number(d, row, col):
            rows[row][d] +=1
            cols[col][d] +=1
            boxes[box_idx(row, col)][d] +=1
            board[row][col] = str(d)
            
        def remove_number(d, row, col):
            del rows[row][d]
            del cols[col][d]
            del boxes[box_idx(row, col)][d]
            board[row][col] = '.'
            
        def place_next_number(row, col):
            if col == N-1 and row == N-1:
                nonlocal sudoku_solved
                sudoku_solved = True
                
            else:
                if col == N-1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)
                    
        def backtrack(row = 0, col = 0):
            if board[row][col] == '.':
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_number(row, col)
                        
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_number(row, col)
                
        
        n = 3
        N = 9
        box_idx = lambda row, col: (row // n ) * n + col // n
        
        rows = [defaultdict(int) for i in range(N)]
        cols = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.': 
                    d = int(board[i][j])
                    place_number(d, i, j)
                    
        sudoku_solved = False
        backtrack()