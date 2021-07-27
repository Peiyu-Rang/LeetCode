# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 17:29:08 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        next_level = deque([root])
        
        while next_level:
            curr_level = next_level
            next_level = deque()
            
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
        return sum([node.val for node in curr_level])