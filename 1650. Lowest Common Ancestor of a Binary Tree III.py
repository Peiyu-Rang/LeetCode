# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 23:39:07 2021

@author: Caven
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def helper(self, node, path):
        if not node:
            return
        path.add(node)
        
        self.helper(node.parent, path)
            
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        path = set()
        self.helper(p, path)
        
        while q:
            if q in path:
                return q
            q = q.parent
        
