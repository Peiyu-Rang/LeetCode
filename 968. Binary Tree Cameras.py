# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 17:38:16 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dp(node):
            if not node:
                return (0,0,float('inf'))
            
            left = dp(node.left)
            right = dp(node.right)
            
            dp0 = left[1] + right[1]
            dp1 = min(left[2] + min(right[1:]), right[2] + min(left[1:]))
            dp2 = 1 + min(left) + min(right)
            
            return (dp0, dp1, dp2)
        
        return min(dp(root)[1:])