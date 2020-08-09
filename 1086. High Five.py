# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 08:41:25 2020

@author: Caven
"""

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dic = {}
        for l in items:
            if l[0] in dic:
                dic[l[0]].append(l[1])
            else:
                dic[l[0]] = [l[1]]
        print(dic)
        return [[key, sum(sorted(dic[key])[-5:])//5] for key in dic]