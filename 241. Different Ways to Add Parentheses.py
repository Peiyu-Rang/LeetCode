# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 22:16:41 2021

@author: Caven
"""


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        listFinal = []
        # Base case.
        if '+' not in expression and '-' not in expression and '*' not in expression:
            listFinal.append(int(expression))

        # Recursive case.
        for i, v in enumerate(expression):
            if v == '+' or v == '-' or v == '*':
                listFirst = self.diffWaysToCompute(expression[0: i])
                listSecond = self.diffWaysToCompute(expression[i + 1: len(expression)])
                for i, valuei in enumerate(listFirst):
                    for j, valuej in enumerate(listSecond):
                        if v == '+':
                            listFinal.append(valuei + valuej)
                        elif v == '-':
                            listFinal.append(valuei - valuej)
                        else:  # v == '*'
                            listFinal.append(valuei * valuej)
        return listFinal
