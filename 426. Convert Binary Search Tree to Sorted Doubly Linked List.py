# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 07:33:53 2021

@author: Caven
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            nonlocal first, last
            if not node:
                return node
            
            helper(node.left)

            if last:
                last.right = node
                node.left = last

            else:
                first = node

            last = node
            helper(node.right)
        
        
        if not root:
            return root
        
        first, last = None, None
        
        helper(root)
        
        last.right = first
        first.left = last
        
        return first