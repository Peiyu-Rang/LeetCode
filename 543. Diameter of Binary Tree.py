# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 16:09:42 2020

@author: Caven
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        
        def depth(node):
            if not node: return 0
            l = depth(node.left)
            r = depth(node.right)
            
            self.ans = max(self.ans, r+l+1)
            
            return max(r,l) + 1
        
        depth(root)
        
        return self.ans -1