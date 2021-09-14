# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 16:21:08 2021

@author: Caven
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        path_split = path.split('/')
        
        for rep in path_split:
            if rep == '..':
                if stack:
                    stack.pop()
            elif rep == '.' or not rep:
                continue
            else:
                stack.append(rep)
                
        return '/' + '/'.join(stack)