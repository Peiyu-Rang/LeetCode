# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:33:37 2021

@author: Caven
"""


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter1 = collections.Counter(s)
        counter2 = collections.Counter(t)
        
        res = [abs(counter1[c] - counter2[c]) for c in 'abcdefghijklmnopqrstuvwxyz']
        
        return sum(res) // 2