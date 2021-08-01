# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:31:40 2020

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSame(x,y):
            if not x and not y:
                return True
            if (not x or not y) or (x.val != y.val):
                return False
            return isSame(x.left, y.left) and isSame(x.right, y.right)
        
        def dfs(x,y):
            if not x or not y:
                return False
            if x.val == y.val:
                if isSame(x,y):
                    return True
            return dfs(x.left, y) or dfs(x.right, y)
        
        return dfs(s,t)
    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSametree(self,p, q):
        if not p and q:
            return False
        elif p and not q:
            return False
        elif not p and not q:
            return True
        elif p.val != q.val:
            return False
        else:
            return self.isSametree(p.left, q.left) and self.isSametree(p.right, q.right)
        
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and not subRoot:
            return True
        if not root:
            return False
        if self.isSametree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    
            
        