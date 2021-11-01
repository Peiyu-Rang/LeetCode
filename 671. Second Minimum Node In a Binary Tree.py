# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 20:52:57 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        smallest = root.val
        res = float('inf')
        
        
        
        def helper(root):
            nonlocal res
            if not root: return 
            if smallest < root.val < res:
                res = root.val
            
            elif root.val == smallest:
                helper(root.left)
                helper(root.right)
                
        
        helper(root)
        return res if res < float('inf') else -1
    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        smallest = root.val
        res = float('inf')
        
        q = deque([root])
        
        while q:
            node = q.popleft()
            
            if node.val == smallest:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            elif smallest < node.val < res:
                res = node.val
                
        return res if res < float('inf') else -1