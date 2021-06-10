# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 07:53:47 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, start, end):
        if start > end:
            return [None]
        all_trees = []
        
        for i in range(start, end + 1):
            left_trees = self.helper(start, i - 1)
            right_trees = self.helper(i + 1, end)
            
            for l in left_trees:
                for r in right_trees:
                    current_tree = TreeNode(i)
                    current_tree.left = l
                    current_tree.right = r
                    all_trees.append(current_tree)
                    
        return all_trees
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.helper(1, n) if n else []