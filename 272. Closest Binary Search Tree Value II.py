# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:11:34 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        max_heap = []
        
        while q:
            node = q.popleft()
                
            heapq.heappush(max_heap, (-abs(node.val - target), node.val))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        return [x[1] for x in max_heap]