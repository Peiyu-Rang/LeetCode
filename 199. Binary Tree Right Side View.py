# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 13:43:00 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        
        while q:
            level_size = len(q)
            level = []
            for i in range(level_size):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            res.append(level[-1])
            
        return res