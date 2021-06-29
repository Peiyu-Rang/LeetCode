# -*- coding: utf-8 -*-
"""
Created on Sun May 23 18:00:38 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
            
        return res
    
    

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root, res = []):
            if root:
                if root.left:
                    helper(root.left, res)
                res.append(root.val)
                if root.right:
                    helper(root.right, res)
                    
        res = []
        helper(root, res)
        return res
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root, res= []):
            if not root:
                return
                
            else:
                helper(root.left, res)
                res.append(root.val)
                helper(root.right, res)
                
        helper(root, res)
        return res