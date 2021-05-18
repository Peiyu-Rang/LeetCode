# -*- coding: utf-8 -*-
"""
Created on Mon May 17 00:11:23 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        dic = {}
        
        res = []
        
        def traverse(root):
            if not root:
                return 'e'
            
            left = traverse(root.left)
            right= traverse(root.right)
            curr = 'L' + left + 'M' + str(root.val) + 'R' + right
            if curr not in dic:
                dic[curr] = 1
            else:
                dic[curr] +=1
                
            if dic[curr] == 2:
                res.append(root)
            
            return curr
        
        traverse(root)
        
        return res