# -*- coding: utf-8 -*-
"""
Created on Sat May 29 13:27:59 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        mapper = {v:i for i,v in enumerate(inorder)}
        
        pre_idx = 0
        
        def helper(left, right):
            nonlocal pre_idx
            # base
            if left > right:
                return
            
            root = TreeNode(preorder[pre_idx])
            pre_idx +=1
            
            mid = mapper[root.val]
            
            root.left  = helper(left,mid-1 )          
            root.right = helper(mid + 1,right)
            
            return root
        
        return helper(0, len(inorder)-1)
    
    
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(preorder, inorder):
            # base
            if not preorder or not inorder:
                return
            
            root = TreeNode(preorder[0])
            
            mid = inorder.index(root.val)
            
            root.left  = helper(preorder[1:mid+1],inorder[:mid] )          
            root.right = helper(preorder[mid+1:],inorder[mid+1:])
            
            return root
        
        return helper(preorder, inorder)