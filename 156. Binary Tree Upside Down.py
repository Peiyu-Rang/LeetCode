# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:44:31 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or (not root.left and not root.right):
            return root
        left = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None
        return left