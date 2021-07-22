# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 02:04:35 2021

@author: Caven
"""


class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.player1row = [0] * n
        self.player1col = [0] * n
        self.player1diag = 0
        self.player1antidiag = 0
        self.player2row = [0] * n
        self.player2col = [0] * n
        self.player2diag = 0
        self.player2antidiag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 1:
            self.player1row[row] +=1
            self.player1col[col] +=1
            if row == col:
                self.player1diag +=1
            if row + col == self.n-1:
                self.player1antidiag +=1
        elif player == 2:
            self.player2row[row] +=1
            self.player2col[col] +=1
            if row == col:
                self.player2diag +=1
            if row + col == self.n-1:
                self.player2antidiag +=1
                
        if max(self.player1row) == self.n or max(self.player1col) == self.n or self.player1diag == self.n or self.player1antidiag == self.n:
            return 1
        elif max(self.player2row) == self.n or max(self.player2col) == self.n or self.player2diag == self.n or self.player2antidiag == self.n:
            return 2
        else:
            return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)