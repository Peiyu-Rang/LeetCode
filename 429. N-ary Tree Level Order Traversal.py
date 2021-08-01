# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:26:38 2021

@author: Caven
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        res = []
        
        while queue:
            level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                queue.extend(curr.children)
                
            res.append(level)
            
        return res
    
    
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        res = []
        
        queue = deque([root])
        
        while queue:
            level = []
            level_len = len(queue)
            
            for i in range(level_len):
                curr = queue.popleft()
                level.append(curr.val)
                
                children = curr.children
                
                for c in children:
                    queue.append(c)
                    
            res.append(level)
            
        return res
        