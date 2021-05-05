# -*- coding: utf-8 -*-
"""
Created on Tue May  4 23:20:13 2021

@author: Caven
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates_counter = Counter(candidates)
        candidates_counter = [(c, candidates_counter[c]) for c in candidates_counter]
        
        res = []
        
        def backtrack(remain, comb, new_start, counter):
            if remain == 0:
                res.append(list(comb))
                return
            elif remain < 0:
                return
            
            for i in range(new_start, len(counter)):
                candidate, freq = counter[i]
                if freq <= 0:
                    continue
                comb.append(candidate)
                counter[i] = (candidate, freq - 1)
                backtrack(remain - candidate, comb, i, counter)
                comb.pop()
                counter[i] = (candidate, freq)
                
        backtrack(target, [], 0, candidates_counter)
        

        
        return res