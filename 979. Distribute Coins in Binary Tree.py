# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 18:09:43 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        res = 0
        
        def dp(node):
            nonlocal res
            if not node:
                return 0
            left = dp(node.left)
            right= dp(node.right)
            
            res += abs(left) + abs(right)
            
            return node.val + left + right -1
        
        dp(root)
        
        return res
        