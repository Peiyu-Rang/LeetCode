# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 23:13:21 2021

@author: Caven
"""


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        
        def solver(n, start, now):
            if now:
                res.append(now+[n])
            
            for i in range(start, int(math.sqrt(n))+1):
                if n%i==0:
                    solver(n//i, i, now+[i])
        
        solver(n,2,[])
        return res