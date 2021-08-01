# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 16:34:29 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
                
        def backtrack(root, remainSum, sequence):
            if not root:
                return 
            sequence.append(root.val)
            
            if remainSum == root.val and not root.left and not root.right:
                res.append(list(sequence))
            else:
                backtrack(root.left, remainSum - root.val, sequence)
                backtrack(root.right, remainSum - root.val, sequence)
                
            sequence.pop()

        backtrack(root, targetSum, [])
        
        
        return res
            
        