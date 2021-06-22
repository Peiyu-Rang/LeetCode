# -*- coding: utf-8 -*-
"""
Created on Sun May 16 14:40:04 2021

@author: Caven
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 3:
            return [[1] * (x + 1) for x in range(numRows)]
        
        res = [[1],[1,1]]
        for i in range(3, numRows + 1):
            last_row = res[-1]
            
            i = 0
            temp = [1]
            while i < len(last_row) - 1:
                temp.append(last_row[i] + last_row[i+1])
                i +=1
                
            temp.append(1)
            
            res.append(temp)
            
        return res
                
            
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if numRows == 1:
            res.append([1])
            return res
        if numRows == 2:
            res.append([1])
            res.append([1,1])
            return res
        res = [[1],[1,1]]
        for i in range(3, numRows + 1):
            last = res[-1]
            new = last + [1]
            n = len(last)
            for j in range(n-1, 0, -1):
                new[j] = last[j] + last[j-1]
            res.append(new)
            
        return res            
        