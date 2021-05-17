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
                
            
            
        