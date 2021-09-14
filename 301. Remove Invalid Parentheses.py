# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 11:05:44 2021

@author: Caven
"""


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        #get the number of invalid left and right parentheses
        #dfs traverse the string, try to remove all possible invalid parentheses compbinations
        #at same level, skip consecutive same symbols, as removing any of them, the new string will be the same
        #roughly O(2^n) time, O(n) for extra space 
        left, right = 0, 0
        for char in s:
            if char == "(":
                left += 1
            if char == ")":
                if left:
                    left -= 1
                else:
                    right += 1
        
        res = []
        self.dfs(s, 0, left, right, res)
        return res
        
    def dfs(self, s, start, left, right, res):
        if left == 0  and right == 0 and self.isValid(s):
            res.append(s)

        for i in range(start, len(s)):
            if i > start and s[i] == s[i-1]:
                continue
            if s[i] in ("()"):
                new = s[:i] + s[i+1:]
                if s[i] == "(":
                    self.dfs(new, i, left - 1, right, res)
                else:
                    self.dfs(new, i, left, right - 1, res)
    
    def isValid(self, s):
        balance = 0
        for char in s:
            if char == "(":
                balance += 1
            if char == ")":
                balance -= 1
                if balance < 0:
                    return False
        return balance == 0