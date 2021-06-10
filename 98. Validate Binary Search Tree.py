# -*- coding: utf-8 -*-
"""
Created on Mon May 31 18:11:02 2021

@author: Caven
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, low = -math.inf, high = math.inf):
        if not node:
            return True
        if node.val <= low or node.val >= high:
            return False
        else:
            return self.helper(node.left, low, node.val) and self.helper(node.right, node.val, high)
        
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        return self.helper(root)