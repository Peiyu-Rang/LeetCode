# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 17:32:29 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        
        stack = [(root, str(root.val))]

        while stack:
            curr, path = stack.pop()
            
            if not curr.left and not curr.right:
                res.append(path)
            
            if curr.right:
                stack.append((curr.right, path + '->' + str(curr.right.val)))
            if curr.left:
                stack.append((curr.left, path + '->' + str(curr.left.val)))
                
            
        return res