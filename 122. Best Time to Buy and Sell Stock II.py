# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:14:19 2020

@author: Caven
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        vally = prices[0]
        peak = prices[0]
        i = 0
        ans = 0
        
        while(i < n-1):
            while(i < n-1 and prices[i] >= prices[i+1]):
                i+=1
            vally = prices[i]
            while(i < n-1 and prices[i] <= prices[i+1]):
                i+=1
            peak = prices[i]
            
            ans += peak-vally
            
        return ans
    
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
                
        return res