# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:06:52 2020

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        sum -= root.val
        
        if not root.left and not root.right:
            return sum == 0
        
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)