# -*- coding: utf-8 -*-
"""
Created on Sun May 16 21:24:04 2021

@author: Caven
"""


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        min_sum = 2000
        dic = {}
        for i,v in enumerate(list1):
            dic[v] = i
        
        for i,v in enumerate(list2):
            if v in dic:
                if i + dic[v] < min_sum:
                    res = [v]
                    min_sum = i + dic[v]
                elif i + dic[v] == min_sum:
                    res.append(v)
                    
        return res