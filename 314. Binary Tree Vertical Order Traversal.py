# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 20:11:21 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_dict = defaultdict(list)
        q = deque([(root, 0)])
        
        while q:
            node, col = q.popleft()
            
            if node:
                col_dict[col].append(node.val)
                q.append((node.left, col - 1))
                q.append((node.right, col + 1))
                
        return [col_dict[x] for x in sorted(col_dict.keys())]