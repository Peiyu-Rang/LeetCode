# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 11:44:47 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_path = 0
        def longestPath(node):
            nonlocal max_path
            if not node:
                return 0
            
            left = longestPath(node.left)
            right= longestPath(node.right)
            
            max_path = max(max_path, left + right)
            
            return max(left, right) + 1
        
        longestPath(root)
        
        return max_path