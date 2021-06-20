# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 21:36:44 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
                
        res = cur = TreeNode()
        for n in inorder(root):
            cur.right = TreeNode(n)
            cur = cur.right
            
        return res.right