# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 08:50:35 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        
        queue = deque([root])
        
        while queue:
            level = []
            level_len = len(queue)
            for i in range(level_len):
                curr = queue.popleft()
                level.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
            res.append(level)
            
        return res[::-1]