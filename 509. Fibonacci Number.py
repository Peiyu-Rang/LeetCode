# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 16:57:41 2020

@author: Caven
"""

class Solution:
    def fib(self, N: int) -> int:
        if N<2:
            return N
        f0 = 0
        f1 = 1
        ans = [0,1]
        for i in range(1,N):
            ans.append(ans[-1] + ans[-2])
        
        return ans[-1]