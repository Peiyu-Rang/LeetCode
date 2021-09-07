# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 21:24:07 2021

@author: Caven
"""


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = collections.defaultdict(list)
        res = 0
        
        for i,v in enumerate(time):
            if v%60 not in dic:
                dic[(60 - v % 60) % 60].append(i)
                
            else:
                res += len(dic[v % 60])
                dic[(60 - v % 60) % 60].append(i)
                
        return res
            