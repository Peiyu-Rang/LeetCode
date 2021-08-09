# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 17:12:33 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        path_sum = 0
        stack = [(root, 0)]
        
        while stack:
            root, curr_num = stack.pop()
            if root:
                curr_num = curr_num * 10 + root.val
                
                if not root.left and not root.right:
                    path_sum += curr_num
                else:
                    stack.append((root.right, curr_num))
                    stack.append((root.left, curr_num))
                    
        return path_sum
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        stack = [(root, 0)]
        
        while stack:
            root, curr_sum = stack.pop()
            
            if root:
                curr_sum = curr_sum * 10 + root.val
                
                if not root.left and not root.right:
                    res += curr_sum
                if root.left:
                    stack.append((root.left, curr_sum))
                if root.right:
                    stack.append((root.right, curr_sum))
                    
        return res
        