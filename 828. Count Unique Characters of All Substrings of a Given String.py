# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 16:52:22 2020

@author: Caven
"""


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        idx = collections.defaultdict(list)
        for i, c in enumerate(s):
            idx[c].append(i)
            
        ans = 0
        
        for a in idx.values():
            a = [-1] + a + [len(s)]
            for i in range(1,len(a)-1):
                ans += (a[i] - a[i-1]) * (a[i+1] - a[i])
                
        return ans