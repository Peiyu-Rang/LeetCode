# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 23:28:25 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if not node:
                return False
            
            left = helper(node.left)
            right = helper(node.right)
            
            mid = node == p or node == q
            
            if mid + left + right > 1:
                self.res = node
                
            return mid or left or right
        
        helper(root)
        
        return self.res