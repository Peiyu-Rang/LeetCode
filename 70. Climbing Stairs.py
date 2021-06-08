# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 15:42:08 2020

@author: Caven
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <3:
            return n
        f1 = 1
        f2 = 2
        for i in range(2,n):
            ans = f1 + f2
            f1 = f2
            f2 = ans
        
        return ans
    
    

class Solution:
    def helper(self,i, n, cache):
        if i > n:
            return 0
        if i == n:
            return 1
        if i in cache:
            return cache[i]
        
        cache[i] = self.helper(i + 1, n, cache) + self.helper(i + 2, n, cache)
        return cache[i]
    def climbStairs(self, n: int) -> int:
        cache = {}
        return self.helper(0,n,cache)