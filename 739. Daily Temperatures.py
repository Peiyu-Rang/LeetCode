# -*- coding: utf-8 -*-
"""
Created on Sun May 23 15:10:44 2021

@author: Caven
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = deque()
        res = [0] * n
        
        for i in range(n-1, -1, -1):
            if stack:
                while (stack and temperatures[stack[-1]] <= temperatures[i]):
                    stack.pop()
                if stack:
                    res[i] = stack[-1] - i
            stack.append(i)
        return res
        