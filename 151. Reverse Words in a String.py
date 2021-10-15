# -*- coding: utf-8 -*-
"""
Created on Sun May 16 19:46:27 2021

@author: Caven
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
    
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(' ')
        n = len(s_list)
        res = []
        for w in range(n-1, -1, -1):
            if s_list[w] != '':
                res.append(s_list[w])
                
        return ' '.join(res)