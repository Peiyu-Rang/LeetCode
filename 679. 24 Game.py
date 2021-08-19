# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 22:12:24 2021

@author: Caven
"""


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        n = len(cards)
        if n == 1:
            if abs(cards[0] - 24) < 0.01:
                return True
            return False
        
        for i in range(n):
            for j in range(i+1, n):
                ci = cards[i]
                cj = cards[j]
                
                possible_comb = [ci+cj, ci-cj, cj-ci, ci * cj]
                if ci:
                    possible_comb.append(cj/ci)
                    
                if cj:
                    possible_comb.append(ci/cj)
                
                for comb in possible_comb:
                    new_cards = [comb]
                    for k in range(n):
                        if k not in (i,j):
                            new_cards.append(cards[k])
                            
                    if self.judgePoint24(new_cards):
                        return True
        return False