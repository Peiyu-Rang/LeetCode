# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 21:35:21 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        
        return root.val
        
    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right

        return root.val
    
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:  
            if not root.left and not root.right:
                root = None

            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
            
            
        return root