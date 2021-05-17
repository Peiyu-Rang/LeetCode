# -*- coding: utf-8 -*-
"""
Created on Sun May 16 19:46:27 2021

@author: Caven
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))