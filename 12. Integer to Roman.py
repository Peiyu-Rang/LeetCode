# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 17:31:01 2021

@author: Caven
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]
        
        roman = ''
        
        for v, l in digits:
            if num == 0:
                break
                
            count, num = divmod(num, v)
            
            roman += l * count
            
        return roman