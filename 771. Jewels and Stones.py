# -*- coding: utf-8 -*-
"""
Created on Mon May 17 00:15:11 2021

@author: Caven
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        
        for s in stones:
            if s in jewels:
                res +=1
                
        return res