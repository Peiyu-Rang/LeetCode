# -*- coding: utf-8 -*-
"""
Created on Sun May 16 19:49:26 2021

@author: Caven
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([x[::-1] for x in s.split()])
        