# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 16:51:46 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def backtrack(node, curr_sum):
            nonlocal count
            if not node:
                return
            
            curr_sum += node.val
            
            if curr_sum == k:
                count +=1
                
            count += h[curr_sum - k]
            
            h[curr_sum] +=1
            
            backtrack(node.left, curr_sum)
            
            backtrack(node.right, curr_sum)
            
            h[curr_sum] -= 1
            
        count, k = 0, targetSum
        h = defaultdict(int)
        
        backtrack(root, 0)
        
        return count