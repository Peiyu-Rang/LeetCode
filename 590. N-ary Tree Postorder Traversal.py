# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:12:46 2021

@author: Caven
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack, res = [root], []
        
        while stack:
            curr = stack.pop()
            if root:
                res.append(curr.val)
            stack.extend(curr.children)
            
        return res[::-1]