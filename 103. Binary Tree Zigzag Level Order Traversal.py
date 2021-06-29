# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 11:36:46 2021

@author: Caven
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        level_list = deque()
        if not root:
            return []
        
        node_queue = deque([root, None])
        is_order_left = True
        
        while len(node_queue)> 0 :
            curr_node = node_queue.popleft()
            
            if curr_node:
                if is_order_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)
                    
                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
                    
        
            else:
                res.append(level_list)
                if len(node_queue) > 0:
                    node_queue.append(None)
                    
                level_list = deque()
                
                is_order_left = not is_order_left
                
        return res