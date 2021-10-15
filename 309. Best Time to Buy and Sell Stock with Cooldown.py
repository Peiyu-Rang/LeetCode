# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:37:08 2021

@author: Caven
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, held, reset = -float('inf'), -float('inf'), 0
        
        for p in prices:
            pre_sold = sold
            sold = held + p
            held = max(held, reset - p)
            reset = max(reset, pre_sold)
            
        return max(sold, reset)