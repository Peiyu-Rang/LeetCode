# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 16:36:29 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_list = []
        
        def BFS(root):
            queue = deque([(root, 0,0)])
            
            while queue:
                node, row, col = queue.popleft()
                if node:
                    node_list.append((col, row, node.val))
                    queue.append((node.left, row + 1, col -1))
                    queue.append((node.right, row+ 1, col + 1))
                    
                    
        BFS(root)
        
        node_list.sort()
        
        res = OrderedDict()
        for col, row, val in node_list:
            if col in res:
                res[col].append(val)
            else:
                res[col] = [val]
        
        return res.values()