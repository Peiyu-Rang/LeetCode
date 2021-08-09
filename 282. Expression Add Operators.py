# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 13:11:02 2021

@author: Caven
"""


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        
        res = []
        
        def backtrack(index, prev, curr, val, string):
            if index == n:
                if val == target and curr == 0:
                    res.append(''.join(string[1:]))
                return
            
            curr = curr * 10 + int(num[index])
            
            curr_str = str(curr)
            
            if curr > 0:
                #no op
                backtrack(index + 1, prev, curr, val, string)
            
            # add
            string.append('+')
            string.append(curr_str)
            
            backtrack(index + 1, curr, 0, val + curr, string)
            string.pop()
            string.pop()
            
            if string:
                
                # sub
                string.append('-')
                string.append(curr_str)
                backtrack(index + 1, -curr, 0, val - curr, string)
                string.pop()
                string.pop()
                
                # mul
                string.append('*')
                string.append(curr_str)
                backtrack(index + 1, curr * prev, 0, val - prev + (curr * prev), string)
                string.pop()
                string.pop()
                
        backtrack(0,0,0,0,[])
        
        return res
                