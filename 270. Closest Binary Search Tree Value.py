# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 09:59:42 2020

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(r):
            if r is None:
                return []
            else:
                return inorder(r.left) + [r.val] + inorder(r.right)
            
        return min(inorder(root), key = lambda x: abs(target -x))
    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        res = root.val
        while root:
            res = min(root.val, res, key = lambda x: abs(x - target))
            root = root.left if root.val > target else root.right
            
        return res