# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 07:33:44 2021

@author: Caven
"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 and k == 1:
            return 0
        
        if k <= 2**(n-1):
            return self.kthGrammar(n-1,k)
        else:
            return self.kthGrammar(n, k-2**(n-1)) * (-1) + 1
        