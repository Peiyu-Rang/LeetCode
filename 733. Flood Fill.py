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
    
    
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return image
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        m = len(image)
        n = len(image[0])
        
        if image[sr][sc] == newColor:
            return image
        
        cur_color = image[sr][sc]
        image[sr][sc] = newColor
        q = deque([(sr,sc)])
        visited = set()
        while q:
            i,j = q.popleft()
            if (i,j) not in visited:
                visited.add((i,j))
            
            neighbors = [[i+d[0], j+d[1]] for d in directions]
            
            for new_i, new_j in neighbors:
                if 0 <= new_i < m and 0 <=new_j<n and image[new_i][new_j] == cur_color and (new_i, new_j) not in visited:
                    image[new_i][new_j] = newColor
                    q.append((new_i, new_j))
                    
        return image