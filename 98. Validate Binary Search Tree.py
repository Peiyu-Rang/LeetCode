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
    def isValidBST(self, root: TreeNode) -> bool:
        
        def helper(node, low = -math.inf, high = math.inf):
            
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
    
        return helper(root)