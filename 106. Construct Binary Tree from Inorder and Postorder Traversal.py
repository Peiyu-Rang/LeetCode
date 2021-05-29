# -*- coding: utf-8 -*-
"""
Created on Sat May 29 10:53:18 2021

@author: Caven
"""


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        mapper = {v:i for i,v in enumerate(inorder)}
        
        def helper(in_idx, post_idx):
            #base condition
            if in_idx > post_idx:
                return
            
            
            root = TreeNode(postorder.pop())
            
            mid = mapper[root.val]
            root.right = helper(mid+1, post_idx)
            root.left  = helper(in_idx, mid-1)
            
            return root
        
        return helper(0, len(postorder)-1)