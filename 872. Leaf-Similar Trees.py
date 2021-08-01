# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 09:09:18 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeaves(self, root):
        if not root:
            return []
        res = []
        queue = deque([root])
        
        while queue:
            level = []
            level_len = len(queue)
            for i in range(level_len):
                curr = queue.pop()
                if not curr.left and not curr.right:
                    res.append(curr.val)
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
                
        
        return res
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if not root1 and root2:
            return False
        if root1 and not root2:
            return False
        
        leaf1 = self.getLeaves(root1)
        leaf2 = self.getLeaves(root2)
        
        left = 0
        n1 = len(leaf1)
        n2 = len(leaf2)
        
        if n1 != n2:
            return False
        
        while left < n1:
            if leaf1[left]!= leaf2[left]:
                return False
            
            left +=1
        
        return True
        