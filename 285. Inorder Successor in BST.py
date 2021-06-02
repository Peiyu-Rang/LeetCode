# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 20:29:52 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None
        
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
            
        return successor