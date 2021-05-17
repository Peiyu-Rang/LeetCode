# -*- coding: utf-8 -*-
"""
Created on Sun May 16 19:26:53 2021

@author: Caven
"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1] * (rowIndex + 1)
        
        res = [1] * 2

        
        for i in range(2, rowIndex+ 1):
            res.append(1)
            for j in range(i-1, 0, -1):
                res[j] = res[j] + res[j-1]
                
                
        return res