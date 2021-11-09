# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 16:44:11 2021

@author: Caven
"""


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not start or not end or not bank or end not in bank:
            return -1
        
        n = len(start)
        q = deque([(start, 0)])
        bankSet = set(bank)
        
        while q:
            curr, level = q.popleft()
            
            for i in range(len(curr)):
                for l in 'ACGT':
                    nei = curr[:i] + l + curr[i+1:]
                    if nei == end:
                        return level + 1
                    if nei in bankSet:
                        q.append((nei, level+1))
                        bankSet.remove(nei)
                        
        return -1
    
            