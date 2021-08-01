# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 07:53:50 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        values = []
        
        def traverse(root):
            if not root:
                return
            
            values.append(root.val)
            traverse(root.left)
            traverse(root.right)
            
        
        traverse(root)
        
        return len(set(values)) == 1