# -*- coding: utf-8 -*-
"""
Created on Mon May 24 23:29:26 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        
        curr = root
        last_visited = None
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            peek = stack[-1]
            if not peek.right or peek.right == last_visited:
                last_visited = stack.pop()
                res.append(last_visited.val)
                
            else:
                curr = peek.right
                
        return res