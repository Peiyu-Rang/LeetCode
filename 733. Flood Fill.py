# -*- coding: utf-8 -*-
"""
Created on Sun May 23 22:35:40 2021

@author: Caven
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        
        ori_color = image[sr][sc]
        
        if ori_color == newColor:
            return image
        
        def dfs(image, sr, sc):
            if (sr < 0 or sc < 0 or sr >= m or sc >= n or image[sr][sc] != ori_color):
                return
            
            image[sr][sc] = newColor
            
            dfs(image, sr + 1, sc)
            dfs(image, sr-1, sc)
            dfs(image, sr, sc+1)
            dfs(image, sr, sc-1)
            
            return image
        
        return dfs(image, sr, sc)