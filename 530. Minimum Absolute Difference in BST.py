# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 23:04:55 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        L = []
        
        def dfs(node):
            if node.left:
                dfs(node.left)
            L.append(node.val)
            if node.right:
                dfs(node.right)
        
        dfs(root)
        res = float('inf')
        
        for i in range(len(L) - 1):
            res = min(res, abs(L[i] - L[i+1]))
            
        return res