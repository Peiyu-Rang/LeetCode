# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 15:54:17 2021

@author: Caven
"""


class Solution:
    def __init__(self):
        self.count = 0
    def countArrangement(self, n: int) -> int:
        visited = [False] * (n+1)
        self.calculate(n, 1, visited)
        
        return self.count
    
    def calculate(self, n, idx, visited):
        if idx > n:
            self.count +=1
        for i in range(1, n+1):
            if (not visited[i]) and (idx % i == 0 or i % idx == 0):
                visited[i] = True
                self.calculate(n, idx + 1, visited)
                visited[i] = False
        