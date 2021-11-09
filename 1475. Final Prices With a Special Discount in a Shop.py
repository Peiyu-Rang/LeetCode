# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 22:11:44 2021

@author: Caven
"""


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        
        for i, p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                prices[stack.pop()] -= p
            
            stack.append(i)
        return prices