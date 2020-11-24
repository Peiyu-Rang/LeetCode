# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:11:41 2020

@author: Caven
"""


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c:i for i, c in enumerate(S)}
        
        j = anchor = 0
        ans = []
        
        for i,c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i-anchor + 1)
                anchor = j+1
        
        return ans