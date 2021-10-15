# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 22:54:41 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        
        arr = inorder(root)
        
        counter = collections.Counter(arr)
        
        maxCount = 0
        res = []
        
        for key in counter:
            if counter[key] > maxCount:
                res = [key]
                maxCount = counter[key]
            elif counter[key] == maxCount:
                res.append(key)
            
                
        return res