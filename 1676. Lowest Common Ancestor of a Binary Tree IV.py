# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 23:29:25 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        node_set = set(nodes)
        
        def dfs(node, node_set):
            if not node:
                return None
            
            if node in node_set:
                return node
            left = dfs(node.left, node_set)
            right= dfs(node.right, node_set)
            
            if left and right:
                return node
            if left:
                return left
            if right:
                return right
            
            return None
        
        return dfs(root, node_set)