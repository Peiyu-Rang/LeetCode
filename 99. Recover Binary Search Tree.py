# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 22:22:48 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        x = y = pred = None
        
        node = root
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
                
            node = stack.pop()
            
            if pred and node.val < pred.val:
                y = node
                if not x:
                    x = pred
                else:
                    break
                    
            pred = node
            node = node.right
            
        x.val, y.val = y.val, x.val
            