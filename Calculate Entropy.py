# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 08:41:13 2021

@author: Caven
"""


class Solution:
    def calculateEntropy(self, input: List[int]) -> float:
        counter = Counter(input)
        n = len(input)
        P = [- (counter[key] / n) * math.log2(counter[key] / n) for key in counter]
        return sum(P)