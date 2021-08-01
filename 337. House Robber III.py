# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 17:47:59 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dp(node):
            if not node:
                return (0,0)
            
            left = dp(node.left)
            right = dp(node.right)
            
            rob = node.val + left[1] + right[1]
            not_rob = max(left) + max(right)
            
            return [rob, not_rob]
        
        return max(dp(root))
        