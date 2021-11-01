# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 20:48:25 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def order(root):
            if not root:
                return 0
            left = order(root.left)
            right = order(root.right)
            
            level = max(left, right) + 1
            
            dic[level].append(root.val)
            
            return level
        
        dic = collections.defaultdict(list)
        
        order(root)
        res = []
        for i in range(1, len(dic) + 1):
            res.append(dic[i])
            
        return res