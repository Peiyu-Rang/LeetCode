# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 07:54:25 2020

@author: Caven
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        nrow = len(image)
        ncol = len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        def dfs(r,c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >=1:
                    dfs(r-1,c)
                if r+1 <= nrow-1:
                    dfs(r+1,c)
                if c >=1:
                    dfs(r, c-1)
                if c+1 <= ncol-1:
                    dfs(r, c+1)
        dfs(sr,sc)
        return image