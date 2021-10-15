# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 21:32:53 2021

@author: Caven
"""


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x: len(x))
        dic = {}
        max_prev = -float('inf')
        for word in words:
            curr_len = 1
            for i in range(len(word)):
                if word[:i] + word[i+1:] in dic:
                    curr_len = max(curr_len, dic[word[:i] + word[i+1:]] + 1)
            dic[word] = curr_len
            max_prev = max(max_prev, curr_len)
            
                         
        
        return max_prev