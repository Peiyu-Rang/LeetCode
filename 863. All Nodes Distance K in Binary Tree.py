# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 21:29:12 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)
                
        dfs(root)
        
        q = collections.deque([(target, 0)])
        
        seen = {target}
        
        while q:
            if q[0][1] == k:
                return [node.val for node, _ in q]
            
            curr, level = q.popleft()
            
            for nei in (curr.left, curr.right, curr.par):
                if nei and nei not in seen:
                    q.append((nei, level + 1))
                    seen.add(nei)
                    
        return []