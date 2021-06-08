# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 22:25:50 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root: TreeNode) -> int:
        if not root:
            return -1
        else:
            return 1 + max(self.height(root.left), self.height(root.right))
        
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return abs(self.height(root.left) -self.height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
        