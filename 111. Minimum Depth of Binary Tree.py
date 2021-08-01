# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 07:30:25 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Depth(self, root: TreeNode) -> int:
        if not root:
            return float('inf')
        
        if not root.left and not root.right:
            return 1
        
        return min(self.Depth(root.left), self.Depth(root.right)) + 1
    
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.Depth(root)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [(1,root)]
        min_depth = float('inf')
        
        while stack:
            depth, root = stack.pop()
            children = [root.left, root.right]
            
            if not any(children):
                min_depth = min(depth, min_depth)
            
            for c in children:
                if c:
                    stack.append((depth+1, c))
                    
        return min_depth