# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 09:30:59 2021

@author: Caven
"""


# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution(object):
    def __init__(self):
        self.q = []
        
    def read(self, buf, n):
        i = 0
        while i < n:
            if self.q:
                buf[i] = self.q.pop(0)
                i += 1
            else:
                buf4 = ['']*4
                v = read4(buf4)
                if v == 0:
                    break
                self.q += buf4[:v]
        return i