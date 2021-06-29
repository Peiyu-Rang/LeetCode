# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 17:49:10 2021

@author: Caven
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        result = []
        self.helper(n, n, '', result)
        return result
    
    def helper(self, l, r, item, result):
        if r < l:
            return
        if l == 0 and r == 0:
            result.append(item)
        if l > 0:
            self.helper(l-1, r, item + '(', result)
        if r > 0:
            self.helper(l, r-1, item + ')', result)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(l, r, item, res):
            if r < l:
                return
            if l == 0 and r ==0:
                res.append(item)
            if l > 0:
                helper(l-1, r, item + '(', res)
            if r > 0:
                helper(l, r-1, item + ')', res)
        
        
        if n == 0:
            return []
        
        res = []
        helper(n, n, '', res)
        return res
    
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        res = []
        def backtrack(l, r, comb):
            if r < l:
                return
            if l == 0 and r == 0:
                res.append(comb)
                return
            
            if l > 0:
                backtrack(l-1, r, comb + '(')
            if r > 0:
                backtrack(l, r-1, comb + ')')
                
        
        backtrack(n, n, '')
        
        return res
        
        