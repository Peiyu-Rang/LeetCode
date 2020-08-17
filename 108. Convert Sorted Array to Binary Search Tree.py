# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 16:29:01 2020

@author: Caven
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        i = 0
        j = n-1
        
        def helper(left, right):
            if left > right:
                return None
            p = (left + right)//2
            node = TreeNode(nums[p])
            node.left = helper(left, p-1)
            node.right = helper(p+1, right)
            
            return node
        
        return helper(i,j)