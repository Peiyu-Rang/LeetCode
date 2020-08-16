# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:01:44 2020

@author: Caven
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(tree1, tree2):
            if tree1 is None and tree2 is None:
                return True
            if tree1 is None or tree2 is None:
                return False
            return (tree1.val == tree2.val) and isMirror(tree1.left, tree2.right) and isMirror(tree1.right, tree2.left)
        
        return isMirror(root, root)