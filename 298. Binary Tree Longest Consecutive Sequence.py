# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 21:02:47 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        maxLen = -float('inf')
        
        def dfs(node, parent, length):
            nonlocal maxLen
            if not node:
                return
            if parent and node.val == parent.val + 1:
                length +=1
            else:
                length = 1
                
            maxLen = max(maxLen, length)
            
            dfs(node.left, node, length)
            dfs(node.right, node, length)
            
        dfs(root, None, 0)
        
        return maxLen