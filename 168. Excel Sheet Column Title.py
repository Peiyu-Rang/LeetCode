# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 14:59:25 2020

@author: Caven
"""

class Solution:
    def convertToTitle(self, n: int) -> str:
        if n <= 0:
            return ""
        l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        output = ""
        while (n-1)//26 > 0:
            output = l[(n-1)%26] + output
            n = (n-1)//26 
        return l[(n-1)%26] + output