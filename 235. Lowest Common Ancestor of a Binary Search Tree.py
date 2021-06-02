# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 22:40:03 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p,q = q, p
        if not root:
            return root
            
        if p.val <= root.val <= q.val:
            return root
        
        elif p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p,q)