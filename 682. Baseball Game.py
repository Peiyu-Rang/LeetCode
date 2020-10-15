# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:45:56 2020

@author: Caven
"""


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        for o in ops:
            if o == '+':
                record.append(record[-1] + record[-2])
            elif o == 'D':
                record.append(record[-1]* 2)
            elif o == 'C':
                record.pop()
            else:
                record.append(int(o))
                
        return sum(record)
        