# -*- coding: utf-8 -*-
"""
Created on Mon May 24 22:53:53 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        
        if not root:
            return root
        
        stack.append(root)
        
        while stack:
            curr = stack.pop()
            if curr:
                res.append(curr.val)
                
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
                
        return res