# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 21:38:02 2021

@author: Caven
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')