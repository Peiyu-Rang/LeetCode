# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 23:17:13 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return []
        
        level = 0
        queue = deque([root])
        while queue:
            levels.append([])
            level_len = len(queue)
            for i in range(level_len):
                node = queue.popleft()
                levels[level].append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            level +=1
            
        return levels
    
    

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return []
        
        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            
            levels[level].append(node.val)
            
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
                
        helper(root, 0)
        return levels
    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return []
        
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
        
        return res