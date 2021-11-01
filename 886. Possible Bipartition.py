# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 17:45:39 2021

@author: Caven
"""


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = {}
        dislikeDic = collections.defaultdict(list)
        
        for u,v in dislikes:
            dislikeDic[u].append(v)
            dislikeDic[v].append(u)
            
        for i in range(1, n+1):
            if i not in color:
                color[i] = 0
                stack = [i]
                
                while stack:
                    node = stack.pop()
                    for nei in dislikeDic[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = 0 if color[node] else 1
                        elif color[nei] == color[node]:
                            return False
        return True
