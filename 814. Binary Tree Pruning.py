# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 09:24:04 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def contains1(root):
            if not root:
                return False
            
            left_contains1 = contains1(root.left)
            right_contains1 = contains1(root.right)
            
            if not left_contains1:
                root.left = None
            if not right_contains1:
                root.right = None
                
            return root.val or left_contains1 or right_contains1
    
        return root if contains1(root) else None